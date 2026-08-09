from fastapi import FastAPI
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import cv2
import time
import threading
from pathlib import Path

from .database import init_db, add_event, recent_events, clear_events
from .detector import MotionZoneDetector

BASE = Path(__file__).resolve().parent.parent

app = FastAPI(
    title="SentinelAI VMS",
    version="1.0"
)

app.mount(
    "/static",
    StaticFiles(directory=str(BASE / "app" / "static")),
    name="static"
)

# --------------------------------------------------
# CAMERA STATE
# --------------------------------------------------

camera = None
camera_lock = threading.Lock()
camera_running = False

detector = MotionZoneDetector()

zone = [120, 80, 520, 360]
camera_name = "Camera-01"

latest = {
    "online": False,
    "event": None,
    "confidence": 0,
    "bbox": None
}


# --------------------------------------------------
# REQUEST MODEL
# --------------------------------------------------

class ZoneRequest(BaseModel):
    x1: int
    y1: int
    x2: int
    y2: int


# --------------------------------------------------
# STARTUP
# --------------------------------------------------

@app.on_event("startup")
def startup():
    init_db()


# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

@app.get("/", response_class=HTMLResponse)
def home():
    return (
        BASE / "app" / "static" / "index.html"
    ).read_text(encoding="utf-8")


# --------------------------------------------------
# CAMERA START
# --------------------------------------------------

@app.post("/api/camera/start")
def start_camera():

    global camera
    global camera_running

    with camera_lock:

        if camera is None or not camera.isOpened():

            camera = cv2.VideoCapture(0)

            camera.set(
                cv2.CAP_PROP_FRAME_WIDTH,
                640
            )

            camera.set(
                cv2.CAP_PROP_FRAME_HEIGHT,
                480
            )

        if camera.isOpened():

            camera_running = True

            latest["online"] = True

            return {
                "success": True,
                "message": "Camera started"
            }

        camera_running = False
        latest["online"] = False

        return {
            "success": False,
            "message": "Unable to open camera"
        }


# --------------------------------------------------
# CAMERA STOP
# --------------------------------------------------

@app.post("/api/camera/stop")
def stop_camera():

    global camera
    global camera_running

    with camera_lock:

        camera_running = False

        if camera is not None:

            if camera.isOpened():
                camera.release()

            camera = None

        latest["online"] = False
        latest["event"] = None
        latest["bbox"] = None
        latest["confidence"] = 0

    return {
        "success": True,
        "message": "Camera stopped"
    }


# --------------------------------------------------
# CAMERA STATUS
# --------------------------------------------------

@app.get("/api/status")
def status():

    return {
        "camera": camera_name,

        "online": camera_running
        and camera is not None
        and camera.isOpened(),

        "active_alerts": len(
            [
                e
                for e in recent_events(20)
                if e["status"] == "ACTIVE"
            ]
        ),

        "events": recent_events(10)
    }


# --------------------------------------------------
# EVENTS
# --------------------------------------------------

@app.get("/api/events")
def events():

    return recent_events(50)


@app.delete("/api/events")
def delete_events():

    clear_events()

    return {
        "ok": True
    }


# --------------------------------------------------
# DETECTION ZONE
# --------------------------------------------------

@app.post("/api/zone")
def set_zone(req: ZoneRequest):

    global zone

    zone = [
        req.x1,
        req.y1,
        req.x2,
        req.y2
    ]

    return {
        "ok": True,
        "zone": zone
    }


# --------------------------------------------------
# VIDEO STREAM
# --------------------------------------------------

def generate_frames():

    global camera
    global camera_running
    global latest

    while camera_running:

        # ------------------------------------------
        # CAMERA SAFETY CHECK
        # ------------------------------------------

        if camera is None:

            break

        if not camera.isOpened():

            camera_running = False
            latest["online"] = False

            break

        # ------------------------------------------
        # READ FRAME
        # ------------------------------------------

        success, frame = camera.read()

        if not success:

            latest["online"] = False

            time.sleep(0.2)

            continue

        latest["online"] = True

        # ------------------------------------------
        # DETECTION ZONE
        # ------------------------------------------

        x1, y1, x2, y2 = zone

        # ------------------------------------------
        # MOTION DETECTION
        # ------------------------------------------

        event, confidence, bbox = detector.detect(
            frame,
            zone
        )

        latest["confidence"] = round(
            confidence,
            2
        )

        latest["bbox"] = bbox

        # ------------------------------------------
        # DRAW RESTRICTED ZONE
        # ------------------------------------------

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 180, 255),
            2
        )

        cv2.putText(
            frame,
            "RESTRICTED ZONE",
            (x1, max(20, y1 - 8)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 180, 255),
            2
        )

        # ------------------------------------------
        # DRAW DETECTION
        # ------------------------------------------

        if bbox:

            bx1, by1, bx2, by2 = bbox

            cv2.rectangle(
                frame,
                (bx1, by1),
                (bx2, by2),
                (0, 0, 255),
                2
            )

            cv2.putText(
                frame,
                "MOTION DETECTED",
                (bx1, max(20, by1 - 8)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.55,
                (0, 0, 255),
                2
            )

        # ------------------------------------------
        # CREATE EVENT
        # ------------------------------------------

        if event:

            event_id, timestamp = add_event(
                camera_name,
                "INTRUSION",
                confidence
            )

            latest["event"] = {
                "id": event_id,
                "timestamp": timestamp,
                "confidence": round(
                    confidence,
                    2
                )
            }

        # ------------------------------------------
        # SENTINEL AI LABEL
        # ------------------------------------------

        cv2.putText(
            frame,
            "SENTINELAI | LIVE",
            (12, 28),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            (80, 220, 120),
            2
        )

        # ------------------------------------------
        # ENCODE FRAME
        # ------------------------------------------

        success, buffer = cv2.imencode(
            ".jpg",
            frame,
            [
                cv2.IMWRITE_JPEG_QUALITY,
                82
            ]
        )

        if not success:
            continue

        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n"
            + buffer.tobytes()
            + b"\r\n"
        )


# --------------------------------------------------
# VIDEO FEED
# --------------------------------------------------

@app.get("/video_feed")
def video_feed():

    return StreamingResponse(
        generate_frames(),
        media_type=(
            "multipart/x-mixed-replace; "
            "boundary=frame"
        )
    )


# --------------------------------------------------
# LIVE STATE
# --------------------------------------------------

@app.get("/api/live")
def live_state():

    return {
        "online": latest["online"],
        "event": latest["event"],
        "confidence": latest["confidence"],
        "zone": zone
    }