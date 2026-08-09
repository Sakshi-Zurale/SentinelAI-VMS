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

> **Monitor → Detect → Alert → Record Event → Investigate**

---

# 🎯 Problem Statement

Traditional surveillance systems often require continuous human monitoring of camera feeds.

This creates several challenges:

- 👁️ Continuous manual monitoring is difficult.
- 🚨 Security events may be missed.
- 📊 Important events are difficult to organize.
- 🔍 Investigating incidents becomes time-consuming.
- 🖥️ Multiple security indicators are often scattered across systems.

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
