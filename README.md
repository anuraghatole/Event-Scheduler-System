# 📅 Event Scheduler System

A modular Python-based RESTful backend app built using **Flask**, designed to let users create, list, update, delete, and get reminders for events — with optional recurring patterns and email notifications.

---

## 🚀 Features

- Create, update, delete events
- View all scheduled events (sorted by start time/earliest first)
- Recurring events (daily, weekly, monthly)
- Reminder system (notifies 1 hour before event)
- JSON file persistence
- Search events by title or description
- Unit testing with Pytest
- Easily testable via Postman

---

## 📂 Folder Structure

```bash
Event-Scheduler-System/
├── app.py                # Flask app entry point
├── config.py             # App configurations
├── events.json           # Persistent storage for events
├── models.py             # Event data model
├── scheduler.py          # Reminder and recurrence scheduler
├── storage.py            # File I/O utilities
├── utils.py              # Time helpers & email utilities
├── requirements.txt      # Python dependencies
└── tests/
    └── test_app.py       # Pytest test cases
```

---

## 🔧 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/anuraghatole/Event-Scheduler-System.git
cd Event-Scheduler-System
```

### 2️⃣ Set Up Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

Output:

```bash
* Running on http://localhost:5000
Scheduler running...
```

---

## 📬 Postman Collection

You can test the API using this [Postman Collection](https://www.postman.com/luckyy15/workspace/anurag-workplace/collection/36430452-7c0bb31d-28e8-44e9-bc26-a416c81608c4?action=share&creator=36430452).

Import it into Postman and run the endpoints as shown.

---

## 📬 API Usage via Postman

### 1. Create Event – `POST /events`

**URL:**  
`http://localhost:5000/events`

**Body (raw → JSON):**

```json
{
  "title": "Team Meeting",
  "description": "Discuss progress",
  "start_time": "2025-07-01T10:00:00",
  "end_time": "2025-07-01T11:00:00",
  "recurrence": "daily"
}
```

---

### 2. List Events – `GET /events`

**URL:**  
`http://localhost:5000/events`

✅ Returns all events, sorted by `start_time`

---

### 3. Search Events – `GET /events?query=Meeting`

**URL:**  
`http://localhost:5000/events?query=Meeting`

✅ Returns matching events based on title/description

---

### 4. Update Event – `PUT /events/<event_id>`

**URL:**  
`http://localhost:5000/events/abc-123...`

**Body:**

```json
{
  "title": "Updated Meeting"
}
```

---

### 5. Delete Event – `DELETE /events/<event_id>`

**URL:**  
`http://localhost:5000/events/abc-123...`

---

## 🔔 Reminder System

- Background thread checks every minute for events **due within the next hour**
- Console will print:

```bash
🔔 Reminder: Team Meeting at 2025-07-01T10:00:00
```

---

## 🧪 Run Tests

Make sure virtual environment is activated.

```bash
pytest tests/
```

Output:

```bash
================== test session starts ==================
collected 5 items

tests/test_app.py .....                         [100%]
```

---

## 📦 Example Output

```bash
POST /events
{
  "id": "4f3a...",
  "title": "Team Meeting",
  "start_time": "2025-07-01T10:00:00",
  ...
}
```

```bash
GET /events
[
  {
    "title": "Team Meeting",
    "start_time": "2025-07-01T10:00:00",
    ...
  }
]
```

---

## 🛠️ Technologies Used

- Python 3.x
- Flask
- Pytest
- JSON for persistence
- Postman for API testing

---

## 🧠 Notes

- You can add a `.env` file to manage SMTP credentials for email.
- Logs/reminders appear in the terminal by default.
- Background tasks start automatically when app runs.

---
