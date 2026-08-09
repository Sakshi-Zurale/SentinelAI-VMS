const video = document.getElementById("video");
const overlay = document.getElementById("videoOverlay");
const cameraButton = document.getElementById("cameraButton");

let running = false;


// ==================================================
// START CAMERA
// ==================================================

async function startCamera() {

    try {

        const response = await fetch(
            "/api/camera/start",
            {
                method: "POST"
            }
        );

        const data = await response.json();

        if (!data.success) {

            alert(
                "Unable to start camera.\n" +
                data.message
            );

            return;
        }

        // Start video stream
        video.src =
            "/video_feed?" +
            new Date().getTime();

        overlay.classList.add("hidden");

        running = true;

        // Change button
        cameraButton.textContent =
            "STOP CAMERA";

        cameraButton.classList.add(
            "stop-button"
        );

        refresh();

    }
    catch (error) {

        console.error(error);

        alert(
            "Camera could not be started."
        );
    }
}


// ==================================================
// STOP CAMERA
// ==================================================

async function stopCamera() {

    try {

        await fetch(
            "/api/camera/stop",
            {
                method: "POST"
            }
        );

        // Stop browser video stream
        video.src = "";

        running = false;

        // Show offline overlay
        overlay.classList.remove(
            "hidden"
        );

        // Change button
        cameraButton.textContent =
            "START CAMERA";

        cameraButton.classList.remove(
            "stop-button"
        );

        refresh();

    }
    catch (error) {

        console.error(error);

        alert(
            "Unable to stop camera."
        );
    }
}


// ==================================================
// TOGGLE CAMERA
// ==================================================

function toggleCamera() {

    if (running) {

        stopCamera();

    }
    else {

        startCamera();

    }
}


// ==================================================
// REFRESH DASHBOARD
// ==================================================

async function refresh() {

    try {

        const [
            statusRes,
            eventsRes
        ] = await Promise.all([

            fetch("/api/status"),

            fetch("/api/events")

        ]);

        const status =
            await statusRes.json();

        const events =
            await eventsRes.json();


        // ------------------------------------------
        // CAMERA COUNT
        // ------------------------------------------

        document.getElementById(
            "cameraStatus"
        ).textContent =
            status.online
                ? "1 / 1"
                : "0 / 1";


        // ------------------------------------------
        // ALERT COUNT
        // ------------------------------------------

        document.getElementById(
            "alertCount"
        ).textContent =
            status.active_alerts;


        // ------------------------------------------
        // EVENT COUNT
        // ------------------------------------------

        document.getElementById(
            "eventCount"
        ).textContent =
            events.length;


        // ------------------------------------------
        // STATUS PILL
        // ------------------------------------------

        const pill =
            document.getElementById(
                "statusPill"
            );


        if (status.online) {

            pill.className =
                "pill online";

            pill.textContent =
                "● ONLINE";

        }
        else {

            pill.className =
                "pill offline";

            pill.textContent =
                "● OFFLINE";
        }


        // ------------------------------------------
        // BUTTON STATE
        // ------------------------------------------

        if (status.online) {

            running = true;

            cameraButton.textContent =
                "STOP CAMERA";

            cameraButton.classList.add(
                "stop-button"
            );

            overlay.classList.add(
                "hidden"
            );

        }
        else {

            running = false;

            cameraButton.textContent =
                "START CAMERA";

            cameraButton.classList.remove(
                "stop-button"
            );

        }


        renderEvents(events);

        renderAlerts(events);

    }
    catch (error) {

        console.log(
            "Refresh error:",
            error
        );
    }
}


// ==================================================
// EVENTS
// ==================================================

function renderEvents(events) {

    const element =
        document.getElementById(
            "events"
        );


    if (!events.length) {

        element.innerHTML =
            '<div class="empty">' +
            'No detections recorded yet' +
            '</div>';

        return;
    }


    element.innerHTML =
        events.map(event => `

        <div class="event-row">

            <div class="event-icon">
                ⚠
            </div>

            <div class="event-main">

                <b>
                    ${event.event_type}
                    •
                    ${event.camera}
                </b>

                <span>
                    ${event.timestamp}
                    •
                    ${event.zone}
                </span>

            </div>

            <div class="confidence">

                ${Math.round(
                    event.confidence * 100
                )}%

            </div>

        </div>

    `).join("");
}


// ==================================================
// ALERTS
// ==================================================

function renderAlerts(events) {

    const active =
        events.filter(
            event =>
                event.status === "ACTIVE"
        );


    const element =
        document.getElementById(
            "alerts"
        );


    if (!active.length) {

        element.innerHTML =
            '<div class="empty">' +
            'No active alerts' +
            '</div>';

        return;
    }


    element.innerHTML =
        active.slice(0, 5)
            .map(event => `

        <div class="alert">

            <b>
                🚨
                ${event.event_type}
                DETECTED
            </b>

            <span>

                ${event.camera}
                •
                ${event.timestamp}
                •
                confidence
                ${Math.round(
                    event.confidence * 100
                )}%

            </span>

        </div>

    `).join("");
}


// ==================================================
// SAVE DETECTION ZONE
// ==================================================

async function saveZone() {

    const body = {

        x1: +document.getElementById(
            "x1"
        ).value,

        y1: +document.getElementById(
            "y1"
        ).value,

        x2: +document.getElementById(
            "x2"
        ).value,

        y2: +document.getElementById(
            "y2"
        ).value
    };


    await fetch(
        "/api/zone",
        {
            method: "POST",

            headers: {
                "Content-Type":
                    "application/json"
            },

            body:
                JSON.stringify(body)
        }
    );


    document.getElementById(
        "zoneMsg"
    ).textContent =
        "✓ Detection zone saved";
}


// ==================================================
// CLEAR ALERTS
// ==================================================

async function clearAlerts() {

    await fetch(
        "/api/events",
        {
            method: "DELETE"
        }
    );

    refresh();
}


// ==================================================
// AUTO REFRESH
// ==================================================

setInterval(
    refresh,
    2500
);


// Initial load
refresh();