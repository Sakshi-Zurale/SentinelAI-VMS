import sqlite3
from pathlib import Path
from datetime import datetime

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "sentinelai.db"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            camera TEXT NOT NULL,
            event_type TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            confidence REAL DEFAULT 0.0,
            zone TEXT DEFAULT 'Restricted Zone',
            status TEXT DEFAULT 'ACTIVE'
        )
    """)
    conn.commit()
    conn.close()

def add_event(camera, event_type, confidence, zone="Restricted Zone"):
    conn = get_conn()
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur = conn.execute(
        """INSERT INTO events(camera,event_type,timestamp,confidence,zone)
           VALUES(?,?,?,?,?)""",
        (camera, event_type, ts, confidence, zone)
    )
    conn.commit()
    event_id = cur.lastrowid
    conn.close()
    return event_id, ts

def recent_events(limit=50):
    conn = get_conn()
    rows = conn.execute(
        "SELECT * FROM events ORDER BY id DESC LIMIT ?", (limit,)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]

def clear_events():
    conn = get_conn()
    conn.execute("DELETE FROM events")
    conn.commit()
    conn.close()
