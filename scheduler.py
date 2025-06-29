# scheduler.py

import threading
import time
from datetime import datetime
from storage import load_events, save_events
from utils import is_upcoming

def reminder_loop():
    while True:
        events = load_events()
        updated = []

        for event in events:
            if is_upcoming(event):
                print(f"🔔 Reminder: {event.title} at {event.start_time}")

            # Reschedule recurring events
            event_dt = datetime.fromisoformat(event.start_time)
            if event.recurrence and event_dt < datetime.now():
                next_time = event.next_occurrence()
                if next_time:
                    event.start_time = next_time.isoformat()

            updated.append(event)

        save_events(updated)
        time.sleep(60)  # Check every minute

def start_scheduler():
    t = threading.Thread(target=reminder_loop, daemon=True)
    t.start()
