# Flask SQLite Todo API

A simple REST API for managing tasks built with Flask and SQLite.

This is a learning backend project that demonstrates:

- Flask routes
- JSON requests
- JSON responses
- HTTP status codes
- SQLite database usage
- CRUD operations
- separating API logic from database logic

---

## Features

- Check if the API is running
- Get all tasks
- Get one task by id
- Create a new task
- Update task `done` status
- Update task `priority`
- Delete one task by id
- Delete all tasks
- Store tasks in SQLite
- Separate Flask routes from SQLite logic

---

## Tech Stack

- Python
- Flask
- SQLite
- REST API
- JSON

---

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

---

## Database Model

The project uses a SQLite database file:

```text
tasks.db
```

The database contains one table:

```text
tasks
```

### Table Columns

| Column     | Type    | Description             |
| ---------- | ------- | ----------------------- |
| `id`       | INTEGER | Unique task id          |
| `title`    | TEXT    | Task title              |
| `done`     | INTEGER | Task status: `0` or `1` |
| `priority` | INTEGER | Task priority           |

### Priority Values

```text
1 → high
2 → normal
3 → low
```

### Example Row

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

---

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

---

## Requirements

```txt
Flask
```

---

## Run the Project

```bash
python app.py
```

The server will start at:

```text
http://127.0.0.1:5000
```

When the app starts, it calls `init_db()` and creates the `tasks` table if it does not exist.

---

## API Routes

| Method   | Route                      | Description               |
| -------- | -------------------------- | ------------------------- |
| `GET`    | `/`                        | Check if Flask is working |
| `GET`    | `/api/tasks`               | Get all tasks             |
| `GET`    | `/api/tasks/<id>`          | Get one task by id        |
| `POST`   | `/api/tasks`               | Create a new task         |
| `PATCH`  | `/api/tasks/done/<id>`     | Update task `done` status |
| `PATCH`  | `/api/tasks/priority/<id>` | Update task `priority`    |
| `DELETE` | `/api/tasks/<id>`          | Delete one task by id     |
| `DELETE` | `/api/tasks`               | Delete all tasks          |

---

# API Examples

---

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
  [2, "practice SQLite", 1, 2],
  [1, "learn Flask", 0, 2]
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

Status code:

```text
200 OK
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

### If Task Does Not Exist

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

---

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

### Done Validation

The `done` value must be:

```text
0 → not done
1 → done
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

---

### Priority Validation

The `priority` value must be:

```text
1 → high
2 → normal
3 → low
```

If `priority` is not `1`, `2`, or `3`:

```json
{
  "error": "priority must be 1, 2 or 3"
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
PATCH /api/tasks/done/1
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

---

### Required Field

The request body must contain:

```text
done
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

---

### Done Validation

The `done` value must be:

```text
0 → not done
1 → done
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

---

### If Task Does Not Exist

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

## Update Task Priority

### Request

```http
PATCH /api/tasks/priority/1
Content-Type: application/json
```

### Body

```json
{
  "priority": 1
}
```

### Response

```json
[1, "learn Flask", 0, 1]
```

Status code:

```text
200 OK
```

---

### Required Field

The request body must contain:

```text
priority
```

If `priority` is missing:

```json
{
  "error": "priority is required"
}
```

Status code:

```text
400 BAD REQUEST
```

---

### Priority Validation

The `priority` value must be:

```text
1 → high
2 → normal
3 → low
```

If `priority` is not `1`, `2`, or `3`:

```json
{
  "error": "priority must be 1, 2 or 3"
}
```

Status code:

```text
400 BAD REQUEST
```

---

### If Task Does Not Exist

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

---

### If Task Does Not Exist

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

After deleting all tasks, the SQLite auto-increment counter is reset.  
The next created task will start again from:

```text
id = 1
```

---

# How It Works

## app.py

`app.py` contains the Flask application and API routes.

It is responsible for:

- receiving HTTP requests
- reading JSON request data
- validating request data
- calling functions from `db.py`
- returning JSON responses
- returning correct HTTP status codes

---

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

---

## Data Flow

### Creating a Task

```text
Client sends POST /api/tasks
→ Flask receives JSON body
→ app.py checks title, done, priority
→ app.py validates done and priority
→ app.py calls create_task(title, done, priority)
→ db.py inserts the task into SQLite
→ SQLite creates a new id
→ db.py returns the new id
→ app.py returns JSON response with the id
```

---

### Getting All Tasks

```text
Client sends GET /api/tasks
→ Flask route is called
→ app.py calls get_all_tasks()
→ db.py reads rows from SQLite
→ db.py returns rows
→ app.py returns rows as JSON
```

---

### Updating Task Done Status

```text
Client sends PATCH /api/tasks/done/<id>
→ Flask receives JSON body
→ app.py checks and validates done
→ app.py calls update_task_done(task_id, done)
→ db.py updates the task in SQLite
→ app.py gets the updated task
→ app.py returns the updated task as JSON
```

---

### Updating Task Priority

```text
Client sends PATCH /api/tasks/priority/<id>
→ Flask receives JSON body
→ app.py checks and validates priority
→ app.py calls update_task_priority(task_id, priority)
→ db.py updates the task in SQLite
→ app.py gets the updated task
→ app.py returns the updated task as JSON
```

---

### Deleting a Task

```text
Client sends DELETE /api/tasks/<id>
→ Flask route is called
→ app.py calls delete_task_by_id(task_id)
→ db.py deletes the task from SQLite
→ app.py returns success message
```

---

# Current Response Format

Tasks are currently returned as lists:

```json
[1, "learn Flask", 0, 2]
```

Meaning:

```text
[ id, title, done, priority ]
```

A future improvement would be returning tasks as JSON objects:

```json
{
  "id": 1,
  "title": "learn Flask",
  "done": 0,
  "priority": 2
}
```

---

# Notes

This is a learning project.

It focuses on:

- Flask routes
- SQLite basics
- CRUD operations
- JSON request and response
- HTTP status codes
- separating API logic from database logic

This project does not include:

- user authentication
- frontend interface
- advanced title validation
- tests
- deployment configuration
- production database setup

---

# Possible Improvements

Future improvements:

- Return tasks as JSON objects instead of lists
- Add better validation for `title`
- Add update route for task title
- Add pagination
- Add tests
- Add Docker support later
- Add deployment instructions later

---

# Status

Current version:

- Basic CRUD works
- SQLite database works
- Flask routes work
- Request validation for `done` works
- Request validation for `priority` works
- Separate database layer exists
- Project is ready for GitHub upload as a learning backend project
