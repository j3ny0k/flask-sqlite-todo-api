# Flask SQLite Todo API

A simple REST API for managing tasks built with Flask and SQLite.

This is a learning backend project that demonstrates basic CRUD operations, routing, JSON requests, JSON responses, and working with a SQLite database through a separate database layer.

## Features

- Get all tasks
- Get one task by id
- Create a new task
- Update task `done` status
- Delete one task by id
- Delete all tasks
- Store data in SQLite
- Separate Flask routes from database logic

## Tech Stack

- Python
- Flask
- SQLite
- REST API
- JSON

## Project Structure

```text
flask-sqlite-todo-api/
│
├── app.py              # Flask routes and API responses
├── db.py               # SQLite database functions
├── requirements.txt    # Project dependencies
├── .gitignore          # Files ignored by Git
└── README.md           # Project documentation
```

## Database Model

The project uses a SQLite database file named `tasks.db`.

The `tasks` table has these columns:

| Column     | Type    | Description             |
| ---------- | ------- | ----------------------- |
| `id`       | INTEGER | Unique task id          |
| `title`    | TEXT    | Task title              |
| `done`     | INTEGER | Task status: `0` or `1` |
| `priority` | INTEGER | Task priority           |

Example task row:

```text
(1, "learn Flask", 0, 2)
```

Meaning:

```text
id       → 1
title    → "learn Flask"
done     → 0
priority → 2
```

## Installation

Clone the repository:

```bash
git clone https://github.com/j3ny0k/flask-sqlite-todo-api.git
cd flask-sqlite-todo-api
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## requirements.txt

```txt
Flask
```

## Run the Project

```bash
python app.py
```

The server will start at:

```text
http://127.0.0.1:5000
```

## API Routes

| Method   | Route             | Description               |
| -------- | ----------------- | ------------------------- |
| `GET`    | `/`               | Check if Flask is working |
| `GET`    | `/api/tasks`      | Get all tasks             |
| `GET`    | `/api/tasks/<id>` | Get one task by id        |
| `POST`   | `/api/tasks`      | Create a new task         |
| `PATCH`  | `/api/tasks/<id>` | Update task `done` status |
| `DELETE` | `/api/tasks/<id>` | Delete one task by id     |
| `DELETE` | `/api/tasks`      | Delete all tasks          |

---

# API Examples

## Home Route

### Request

```http
GET /
```

### Response

```json
{
  "message": "Flask is working"
}
```

Status code:

```text
200 OK
```

---

## Get All Tasks

### Request

```http
GET /api/tasks
```

### Response

```json
[
  [1, "learn Flask", 0, 2],
  [2, "practice SQLite", 1, 2]
]
```

Status code:

```text
200 OK
```

If there are no tasks:

```json
[]
```

---

## Get Task by ID

### Request

```http
GET /api/tasks/1
```

### Response

```json
[1, "learn Flask", 0, 2]
```

Status code:

```text
200 OK
```

### If task does not exist

```json
{
  "error": "task not found"
}
```

Status code:

```text
404 NOT FOUND
```

---

## Create Task

### Request

```http
POST /api/tasks
Content-Type: application/json
```

### Body

```json
{
  "title": "learn Flask",
  "done": 0,
  "priority": 2
}
```

### Response

```json
{
  "id": 1
}
```

Status code:

```text
201 CREATED
```

### Required Fields

The request body must contain:

```text
title
done
priority
```

If one of these fields is missing:

```json
{
  "error": "title, done and priority are required"
}
```

Status code:

```text
400 BAD REQUEST
```

---

## Update Task Done Status

### Request

```http
PATCH /api/tasks/1
Content-Type: application/json
```

### Body

```json
{
  "done": 1
}
```

### Response

```json
[1, "learn Flask", 1, 2]
```

Status code:

```text
200 OK
```

### Validation

The `done` value must be:

```text
0 → not done
1 → done
```

If `done` is missing:

```json
{
  "error": "done is required"
}
```

Status code:

```text
400 BAD REQUEST
```

If `done` is not `0` or `1`:

```json
{
  "error": "done must be 0 or 1"
}
```

Status code:

```text
400 BAD REQUEST
```

If task does not exist:

```json
{
  "error": "task not found"
}
```

Status code:

```text
404 NOT FOUND
```

---

## Delete Task by ID

### Request

```http
DELETE /api/tasks/1
```

### Response

```json
{
  "message": "task deleted"
}
```

Status code:

```text
200 OK
```

### If task does not exist

```json
{
  "error": "task not found"
}
```

Status code:

```text
404 NOT FOUND
```

---

## Delete All Tasks

### Request

```http
DELETE /api/tasks
```

### Response

```json
{
  "deleted": 3
}
```

Status code:

```text
200 OK
```

If there were no tasks:

```json
{
  "deleted": 0
}
```

Status code:

```text
200 OK
```

After deleting all tasks, the SQLite auto-increment counter is reset. The next created task will start again from `id = 1`.

---

# How It Works

## app.py

`app.py` contains the Flask application and API routes.

It is responsible for:

- receiving HTTP requests
- reading JSON request data
- calling functions from `db.py`
- returning JSON responses
- returning correct status codes

## db.py

`db.py` contains all SQLite logic.

It is responsible for:

- connecting to `tasks.db`
- creating the `tasks` table
- inserting tasks
- selecting tasks
- updating tasks
- deleting tasks
- committing database changes
- closing the database connection

## Data Flow

Example for creating a task:

```text
Client sends POST /api/tasks
→ Flask receives JSON body
→ app.py reads title, done, priority
→ app.py calls create_task(title, done, priority)
→ db.py inserts the task into SQLite
→ SQLite creates a new id
→ db.py returns the new id
→ app.py returns JSON response
```

Example for getting all tasks:

```text
Client sends GET /api/tasks
→ Flask route is called
→ app.py calls get_all_tasks()
→ db.py reads rows from SQLite
→ app.py returns rows as JSON
```

---

# Notes

This is a learning project.

It focuses on:

- Flask routes
- SQLite basics
- CRUD operations
- JSON request and response
- separating API logic from database logic

This project does not include:

- user authentication
- frontend interface
- advanced validation
- deployment configuration
- production database setup

---

# Possible Improvements

Future improvements:

- Return tasks as JSON objects instead of lists
- Add better validation for `title`, `done`, and `priority`
- Add update route for task title and priority
- Add pagination
- Add tests
- Add Docker support later
- Add deployment instructions later

Example of a better future response format:

```json
{
  "id": 1,
  "title": "learn Flask",
  "done": 0,
  "priority": 2
}
```

Current response format:

```json
[1, "learn Flask", 0, 2]
```

---

# Status

Current version:

- Basic CRUD works
- SQLite database works
- Flask routes work
- Project is ready for first GitHub upload as a learning backend project
