# utils.py

from datetime import datetime

def is_upcoming(event):
    """Check if event is within the next hour."""
    now = datetime.now()
    event_time = datetime.fromisoformat(event.start_time)
    return 0 <= (event_time - now).total_seconds() <= 3600

def matches_query(event, query):
    """Search for a query in title or description."""
    query = query.lower()
    return query in event.title.lower() or query in event.description.lower()
