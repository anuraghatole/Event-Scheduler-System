# app.py

from flask import Flask, request, jsonify
from models import Event
from storage import load_events, save_events
from utils import matches_query
from scheduler import start_scheduler

app = Flask(__name__)
start_scheduler()

@app.route("/events", methods=["POST"])
def create_event():
    try:
        data = request.json
        event = Event(**data)
        events = load_events()
        events.append(event)
        save_events(events)
        return jsonify(event.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/events", methods=["GET"])
def list_events():
    query = request.args.get("query")
    events = load_events()
    if query:
        events = [e for e in events if matches_query(e, query)]
    events.sort(key=lambda e: e.start_time)
    return jsonify([e.to_dict() for e in events])

@app.route("/events/<event_id>", methods=["PUT"])
def update_event(event_id):
    data = request.json
    events = load_events()
    for event in events:
        if event.id == event_id:
            for key, val in data.items():
                setattr(event, key, val)
            save_events(events)
            return jsonify(event.to_dict())
    return jsonify({"error": "Not found"}), 404

@app.route("/events/<event_id>", methods=["DELETE"])
def delete_event(event_id):
    events = load_events()
    updated = [e for e in events if e.id != event_id]
    if len(updated) == len(events):
        return jsonify({"error": "Not found"}), 404
    save_events(updated)
    return jsonify({"message": "Deleted"})
    
if __name__ == "__main__":
    app.run(debug=True)
