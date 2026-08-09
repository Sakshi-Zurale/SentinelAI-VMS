import cv2
import time
import numpy as np

class MotionZoneDetector:
    """
    Fast dependency-light detector for the urgent MVP.
    It detects frame-to-frame motion and triggers an intrusion event
    only when motion overlaps the configured rectangular zone.
    """

    def __init__(self):
        self.prev_gray = None
        self.last_event_time = 0
        self.cooldown = 3.0

    def detect(self, frame, zone):
        x1, y1, x2, y2 = zone
        h, w = frame.shape[:2]
        x1, x2 = max(0, min(x1,w-1)), max(0, min(x2,w-1))
        y1, y2 = max(0, min(y1,h-1)), max(0, min(y2,h-1))

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if self.prev_gray is None:
            self.prev_gray = gray
            return False, 0.0, None

        diff = cv2.absdiff(self.prev_gray, gray)
        thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)

        # Only evaluate motion inside the restricted zone.
        zone_mask = np.zeros_like(thresh)
        zone_mask[y1:y2, x1:x2] = 255
        inside = cv2.bitwise_and(thresh, zone_mask)

        motion_pixels = cv2.countNonZero(inside)
        zone_area = max(1, (x2-x1)*(y2-y1))
        ratio = motion_pixels / zone_area

        triggered = ratio > 0.008
        confidence = min(0.99, 0.55 + ratio * 8)

        bbox = None
        if triggered:
            ys, xs = np.where(inside > 0)
            if len(xs):
                bx1, bx2 = int(xs.min()), int(xs.max())
                by1, by2 = int(ys.min()), int(ys.max())
                bbox = (bx1, by1, bx2, by2)

        self.prev_gray = gray

        # Prevent alert spam.
        if triggered and time.time() - self.last_event_time < self.cooldown:
            return False, confidence, bbox

        if triggered:
            self.last_event_time = time.time()
            return True, confidence, bbox

        return False, confidence, bbox
