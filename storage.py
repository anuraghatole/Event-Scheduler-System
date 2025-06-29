# storage.py

import json
import os
from config import EVENT_FILE_PATH
from models import Event

def load_events():
    if not os.path.exists(EVENT_FILE_PATH):
        return []
    with open(EVENT_FILE_PATH, "r") as f:
        data = json.load(f)
    return [Event.from_dict(d) for d in data]

def save_events(events):
    with open(EVENT_FILE_PATH, "w") as f:
        json.dump([e.to_dict() for e in events], f, indent=2)
