# SentinelAI — Smart Video Management System

A competition-ready prototype for the A-1 Launchpad 2026 Smart Video Management System case study.

## Features
- Live webcam/video stream
- Motion/intrusion detection
- Configurable rectangular detection zone
- Event timestamps
- Event list
- Timeline markers
- Camera status
- Active alerts
- Storage usage
- SQLite event database
- Optional YOLO integration point

## Quick Start

### 1. Create environment
```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```

macOS/Linux:
```bash
source venv/bin/activate
```

### 2. Install
```bash
pip install -r requirements.txt
```

### 3. Run
```bash
uvicorn app.main:app --reload
```

Open:
http://127.0.0.1:8000

Allow browser camera access if prompted.

## Demo
1. Click START CAMERA.
2. Draw a restricted zone on the video.
3. Walk into the zone.
4. SentinelAI detects motion inside the zone.
5. An intrusion event appears in the event list and timeline.
6. Use CLEAR ALERTS to reset the demo.

## Optional YOLO
The first urgent MVP uses OpenCV motion detection so the project runs without downloading a large AI model.
For the final version, add `ultralytics` and a YOLO model in `models/`; the detection service can then be upgraded to object-aware detection.

## Project Structure
```text
SentinelAI_VMS/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── detector.py
│   └── static/
│       ├── index.html
│       ├── style.css
│       └── app.js
├── data/
├── models/
├── recordings/
├── uploads/
├── requirements.txt
└── README.md
```
