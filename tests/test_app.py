# tests/test_app.py

import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()

def test_create_event(client):
    res = client.post("/events", json={
        "title": "SearchTest",
        "description": "Event for search",
        "start_time": "2025-07-01T10:00:00",
        "end_time": "2025-07-01T11:00:00"
    })
    assert res.status_code == 201
    assert res.get_json()["title"] == "SearchTest"

def test_list_events_sorted(client):
    res = client.get("/events")
    assert res.status_code == 200
    data = res.get_json()
    assert isinstance(data, list)
    assert all(data[i]["start_time"] <= data[i+1]["start_time"] for i in range(len(data)-1))

def test_search(client):
    res = client.get("/events?query=SearchTest")
    assert res.status_code == 200
    data = res.get_json()
    assert any("SearchTest" in e["title"] for e in data)

def test_update_event(client):
    # Get the ID of first event
    res = client.get("/events")
    event_id = res.get_json()[0]["id"]
    update = client.put(f"/events/{event_id}", json={"title": "Updated Title"})
    assert update.status_code == 200
    assert update.get_json()["title"] == "Updated Title"

def test_delete_event(client):
    # Create and then delete
    res = client.post("/events", json={
        "title": "ToDelete",
        "description": "Will be deleted",
        "start_time": "2025-07-01T10:00:00",
        "end_time": "2025-07-01T11:00:00"
    })
    event_id = res.get_json()["id"]
    del_res = client.delete(f"/events/{event_id}")
    assert del_res.status_code == 200
