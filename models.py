# models.py

import uuid
from datetime import datetime, timedelta

class Event:
    def __init__(self, title, description, start_time, end_time, recurrence=None, id=None):
        self.id = id or str(uuid.uuid4())
        self.title = title
        self.description = description
        self.start_time = start_time
        self.end_time = end_time
        self.recurrence = recurrence  # daily, weekly, monthly

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Event(
            title=data["title"],
            description=data["description"],
            start_time=data["start_time"],
            end_time=data["end_time"],
            recurrence=data.get("recurrence"),
            id=data["id"]
        )

    def next_occurrence(self):
        dt = datetime.fromisoformat(self.start_time)
        if self.recurrence == "daily":
            return dt + timedelta(days=1)
        elif self.recurrence == "weekly":
            return dt + timedelta(weeks=1)
        elif self.recurrence == "monthly":
            return dt + timedelta(days=30)
        return None
