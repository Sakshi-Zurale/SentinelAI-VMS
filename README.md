# 🛡️ SentinelAI VMS

### AI-Powered Video Management System for Intelligent Surveillance

<p align="center">

  <img src="https://img.shields.io/badge/Python-3.13+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-0.116+-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />

</p>

<p align="center">

  <img src="https://img.shields.io/badge/Status-Prototype-success?style=flat-square" />
  <img src="https://img.shields.io/badge/Platform-Windows-lightgrey?style=flat-square" />
  <img src="https://img.shields.io/badge/Interface-Web%20Dashboard-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/License-Educational-orange?style=flat-square" />

</p>

---

## 🚨 What is SentinelAI VMS?

**SentinelAI VMS** is a computer-vision-powered **Video Management System (VMS)** designed to provide centralized surveillance monitoring through a modern web dashboard.

The system connects to a live camera feed, monitors a configurable restricted zone, detects suspicious motion, generates intrusion events, and presents security information through a centralized dashboard.

Instead of simply displaying a camera feed, SentinelAI VMS focuses on turning surveillance footage into **actionable security events**.

> **Monitor → Detect → Alert → Log → Investigate**

---

# 🎯 Problem Statement

Traditional surveillance systems often require continuous human monitoring of camera feeds.

This creates several challenges:

- 👁️ Continuous manual monitoring is difficult.
- 🚨 Security events may be missed.
- 📊 Important events are difficult to organize.
- 🔍 Investigating incidents becomes time-consuming.
- 🖥️ Security information may be scattered across different systems.

SentinelAI VMS addresses these challenges by providing a **centralized surveillance dashboard with automated computer-vision-based event detection and alerting.**

---

# 💡 Our Solution

SentinelAI VMS provides a centralized interface where a security operator can:

```text
        📷 LIVE CAMERA
              │
              ▼
      🔎 COMPUTER VISION
              │
              ▼
       🚧 DETECTION ZONE
              │
              ▼
       MOTION DETECTION
              │
        ┌─────┴─────┐
        │           │
       SAFE      INTRUSION
        │           │
        │           ▼
        │       🚨 ALERT
        │           │
        └─────┬─────┘
              ▼
        EVENT LOGGING
              │
              ▼
        VMS DASHBOARD
```

---

# ✨ Key Features

### 📷 Live Camera Monitoring

View the connected camera directly through the web-based VMS dashboard.

### 🟢 Camera Status Monitoring

The dashboard provides clear camera availability information:

- ONLINE
- OFFLINE
- Camera started
- Camera stopped

### ▶️ Start / Stop Camera

The operator can control the camera directly from the dashboard.

### 🚧 Configurable Detection Zone

Define a restricted rectangular area that should be monitored for suspicious activity.

### 🔎 Motion Detection

OpenCV-based computer vision continuously analyzes camera frames for movement.

### 🚨 Intrusion Alerts

Motion detected within the configured monitoring zone can generate an intrusion event.

### 📋 Event History

Security events are logged with relevant information such as:

- Camera
- Event type
- Timestamp
- Detection confidence

### 💾 Persistent Event Storage

Events are stored using SQLite for structured retrieval and monitoring.

### 📊 Centralized Dashboard

The dashboard provides a unified view of:

- Camera status
- Active alerts
- Security events
- Detection zone
- Live video
- Event timeline

### 🎨 Modern VMS Interface

The system uses a dark security-dashboard design inspired by professional surveillance platforms.

---

# 🏗️ System Architecture

```text
┌─────────────────────────────────────────────┐
│                 CAMERA INPUT                │
│              Laptop / USB Camera            │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────┐
│             OPENCV VIDEO CAPTURE            │
│        Frame acquisition & processing       │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────┐
│              DETECTION ENGINE               │
│        Motion & restricted-zone check       │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
              ┌────────────────┐
              │ Event detected?│
              └───────┬────────┘
                      │
             ┌────────┴────────┐
             │                 │
            NO                YES
             │                 │
             ▼                 ▼
        Continue         Intrusion Event
                               │
                               ▼
                      ┌─────────────────┐
                      │ Alert Generation│
                      └────────┬────────┘
                               │
                ┌──────────────┼──────────────┐
                ▼              ▼              ▼
             Dashboard      SQLite        Timeline
```

---

# 🧩 Technology Stack

| Layer | Technology |
|---|---|
| Frontend | HTML5, CSS3, JavaScript |
| Backend | Python, FastAPI |
| Computer Vision | OpenCV |
| Database | SQLite |
| API | REST API |
| Server | Uvicorn |
| Development | VS Code |
| Version Control | Git & GitHub |

---

# 📁 Project Structure

```text
SentinelAI_VMS/
│
├── app/
│   │
│   ├── main.py
│   │      └── FastAPI application & API endpoints
│   │
│   ├── detector.py
│   │      └── Computer vision / detection logic
│   │
│   ├── database.py
│   │      └── Database operations
│   │
│   └── static/
│       │
│       ├── index.html
│       │      └── VMS dashboard structure
│       │
│       ├── app.js
│       │      └── Frontend interaction & API communication
│       │
│       └── style.css
│              └── Dashboard styling
│
├── data/
│      └── Application data / database files
│
├── models/
│      └── Detection model resources
│
├── uploads/
│      └── Uploaded / generated resources
│
├── requirements.txt
│      └── Python dependencies
│
├── .gitignore
│      └── Git exclusion rules
│
└── README.md
       └── Project documentation
```

---

# ⚙️ Installation & Setup

## Prerequisites

Make sure you have:

- Python 3.13+
- Git
- Webcam / USB camera
- Modern web browser

---

## 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/SentinelAI-VMS.git
```

```bash
cd SentinelAI-VMS
```

---

## 2. Create Virtual Environment

### Windows

```powershell
python -m venv venv
```

Activate the environment:

```powershell
venv\Scripts\activate
```

---

## 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

---

## 4. Start Server

```powershell
uvicorn app.main:app --reload
```

---

## 5. Open Dashboard

Open your browser:

```text
http://127.0.0.1:8000
```

---

# 🎮 Usage

### 1. Start Monitoring

Click:

```text
▶ START CAMERA
```

Allow webcam access if requested.

### 2. Configure Detection Zone

Set the detection-zone parameters from the dashboard.

### 3. Monitor Live Feed

Observe the live camera feed and configured restricted area.

### 4. Detect Intrusion

When motion occurs inside the configured detection zone, the system generates a security event.

### 5. Review Events

Detected events appear in the dashboard event panel.

### 6. Stop Monitoring

Click:

```text
■ STOP CAMERA
```

The webcam is released safely.

---

# 🔌 API Overview

The backend is powered by FastAPI.

Typical operations include:

```text
GET   /
GET   /api/status
GET   /api/events
GET   /api/camera/stream
POST  /api/camera/start
POST  /api/camera/stop
```

> The exact endpoints may evolve as the project is extended.

---

# 🛡️ Security & Privacy

SentinelAI VMS follows a local-first prototype architecture.

### Current approach

- Camera processing is performed locally.
- No external cloud camera service is required.
- Event information is stored locally.
- Camera control is available directly from the dashboard.

> **Privacy Note:** Appropriate consent and applicable regulations should always be considered before deploying surveillance systems in real-world environments.

---

# 📈 Current Project Status

### MVP / Competition Prototype

| Component | Status |
|---|:---:|
| Web Dashboard | ✅ |
| Live Camera | ✅ |
| Start Camera | ✅ |
| Stop Camera | ✅ |
| Camera Status | ✅ |
| Detection Zone | ✅ |
| Motion Detection | ✅ |
| Intrusion Events | ✅ |
| Alert Panel | ✅ |
| Event History | ✅ |
| SQLite Storage | ✅ |
| REST API | ✅ |
| YOLO Object Detection | 🔜 |
| Multi-Camera Support | 🔜 |
| Automatic Incident Recording | 🔜 |
| Historical Video Playback | 🔜 |
| Advanced AI Analytics | 🔜 |

---

# 🔮 Future Roadmap

## Phase 1 — Current MVP

```text
Live Camera
     ↓
Motion Detection
     ↓
Restricted Zone
     ↓
Intrusion Alert
     ↓
Event Logging
```

## Phase 2 — AI Intelligence

```text
Camera
   ↓
YOLO Object Detection
   ↓
Person / Vehicle Classification
   ↓
Zone Analysis
   ↓
Intelligent Intrusion Detection
```

## Phase 3 — Incident Management

```text
Intrusion
   ↓
Snapshot
   ↓
Automatic Video Recording
   ↓
Incident Timeline
   ↓
Playback
```

## Phase 4 — Enterprise VMS

```text
Multiple Cameras
       ↓
Central VMS
       ↓
AI Analytics
       ↓
Cloud / Local Storage
       ↓
Advanced Reports
       ↓
Role-Based Access
```

---

# 🏆 Potential Use Cases

SentinelAI VMS can be adapted for:

- 🏭 Industrial facilities
- 🏢 Offices
- 🏫 Educational campuses
- 🏪 Retail stores
- 🏠 Residential security
- 🚧 Restricted areas
- 🏗️ Construction sites
- 🅿️ Parking/security monitoring

---

# 🌟 Why SentinelAI VMS?

### Traditional Surveillance

```text
Camera
  ↓
Human Watches
  ↓
Human Notices Event
  ↓
Manual Investigation
```

### SentinelAI VMS

```text
Camera
  ↓
Computer Vision
  ↓
Automated Detection
  ↓
Real-Time Alert
  ↓
Structured Event
  ↓
Centralized Monitoring
```

> ## **Turn passive video surveillance into proactive security intelligence.**

---

# 🎥 Project Demonstration

The demonstration video will showcase:

- Live camera monitoring
- Camera start/stop functionality
- Restricted-zone configuration
- Motion/intrusion detection
- Real-time alerts
- Event logging
- Centralized VMS dashboard

### Demo Video

**[▶ Watch Project Demonstration](ADD-YOUR-VIDEO-LINK-HERE)**

---

# 👩‍💻 Team

## SentinelAI Team

**Developed for:**  
A-1 Launchpad Case Study 2026

**Domain:**  
Video Management & Intelligent Surveillance

---

# 📜 License

This project is developed for **educational, research, and competition purposes**.

---

# ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

<p align="center">

# 🛡️ SentinelAI VMS

### See. Detect. Alert. Secure.

</p>
