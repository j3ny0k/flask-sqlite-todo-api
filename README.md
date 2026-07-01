# Flask SQLite Todo API

A simple REST API for managing tasks built with Flask and SQLite.

This is a learning backend project that demonstrates:

- Flask routes
- JSON requests
- JSON responses
- HTTP status codes
- SQLite database usage
- CRUD operations
- request validation
- query parameters
- separating API logic from database logic

---

## Features

- Check if the API is running
- Get all tasks
- Get task statistics
- Get one task by id
- Filter tasks by `done`
- Filter tasks by `priority`
- Filter tasks by `done` and `priority` together
- Create a new task
- Update task `title`
- Update task `done` status
- Update task `priority`
- Delete one task by id
- Delete all tasks
- Store tasks in SQLite
- Separate Flask routes from SQLite logic
- Return tasks as JSON objects
- Validate `title`, `done`, and `priority`

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

### Done Values

```text
0 → not done
1 → done
```

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

| Method   | Route                      | Description                     |
| -------- | -------------------------- | ------------------------------- |
| `GET`    | `/`                        | Check if Flask is working       |
| `GET`    | `/api/tasks`               | Get all tasks or filtered tasks |
| `GET`    | `/api/tasks/stats`         | Get task statistics             |
| `GET`    | `/api/tasks/<id>`          | Get one task by id              |
| `POST`   | `/api/tasks`               | Create a new task               |
| `PATCH`  | `/api/tasks/title/<id>`    | Update task `title`             |
| `PATCH`  | `/api/tasks/done/<id>`     | Update task `done` status       |
| `PATCH`  | `/api/tasks/priority/<id>` | Update task `priority`          |
| `DELETE` | `/api/tasks/<id>`          | Delete one task by id           |
| `DELETE` | `/api/tasks`               | Delete all tasks                |

---

# API Examples

Base URL:

```text
http://127.0.0.1:5000
```

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
  {
    "id": 2,
    "title": "practice SQLite",
    "done": 1,
    "priority": 2
  },
  {
    "id": 1,
    "title": "learn Flask",
    "done": 0,
    "priority": 2
  }
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

## Query Filters

The `GET /api/tasks` route supports query filters.

Supported filters:

```text
done
priority
```

The filters can be used separately or together.

---

### Filter Tasks by Done Status

### Request

```http
GET /api/tasks?done=0
```

Returns tasks where:

```text
done = 0
```

Meaning:

```text
not done
```

### Response

```json
[
  {
    "id": 1,
    "title": "learn Flask",
    "done": 0,
    "priority": 2
  }
]
```

Status code:

```text
200 OK
```

---

### Request

```http
GET /api/tasks?done=1
```

Returns tasks where:

```text
done = 1
```

Meaning:

```text
done
```

### Response

```json
[
  {
    "id": 2,
    "title": "practice SQLite",
    "done": 1,
    "priority": 2
  }
]
```

Status code:

```text
200 OK
```

---

### Done Query Validation

The `done` query value must be:

```text
0
1
```

Invalid request:

```http
GET /api/tasks?done=abc
```

Response:

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

## Filter Tasks by Priority

### Request

```http
GET /api/tasks?priority=1
```

Returns tasks where:

```text
priority = 1
```

Meaning:

```text
high priority
```

### Response

```json
[
  {
    "id": 1,
    "title": "learn Flask",
    "done": 0,
    "priority": 1
  }
]
```

Status code:

```text
200 OK
```

---

### Request

```http
GET /api/tasks?priority=2
```

Returns tasks where:

```text
priority = 2
```

Meaning:

```text
normal priority
```

### Response

```json
[
  {
    "id": 2,
    "title": "practice SQLite",
    "done": 1,
    "priority": 2
  }
]
```

Status code:

```text
200 OK
```

---

### Request

```http
GET /api/tasks?priority=3
```

Returns tasks where:

```text
priority = 3
```

Meaning:

```text
low priority
```

### Response

```json
[
  {
    "id": 3,
    "title": "read documentation",
    "done": 0,
    "priority": 3
  }
]
```

Status code:

```text
200 OK
```

---

### Priority Query Validation

The `priority` query value must be:

```text
1
2
3
```

Invalid request:

```http
GET /api/tasks?priority=abc
```

Response:

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

## Combined Query Filters

The `done` and `priority` filters can be used together.

### Request

```http
GET /api/tasks?done=0&priority=2
```

Returns tasks where:

```text
done = 0
priority = 2
```

Meaning:

```text
not done and normal priority
```

### Response

```json
[
  {
    "id": 1,
    "title": "learn Flask",
    "done": 0,
    "priority": 2
  }
]
```

Status code:

```text
200 OK
```

---

## Get Task Statistics

### Request

```http
GET /api/tasks/stats
```

### Response

```json
{
  "total": 5,
  "done": 2,
  "not_done": 3,
  "by_priority": {
    "1": 1,
    "2": 3,
    "3": 1
  }
}
```

Status code:

```text
200 OK
```

### Response Fields

```text
total      → total number of tasks
done       → number of completed tasks
not_done   → number of not completed tasks
by_priority → number of tasks grouped by priority
```

Priority keys:

```text
"1" → priority 1
"2" → priority 2
"3" → priority 3
```

If there are no tasks:

```json
{
  "total": 0,
  "done": 0,
  "not_done": 0,
  "by_priority": {
    "1": 0,
    "2": 0,
    "3": 0
  }
}
```

Status code:

```text
200 OK
```

This is not an error. It means the database is working, but there are no tasks yet.

---

## Get Task by ID

### Request

```http
GET /api/tasks/1
```

### Response

```json
{
  "id": 1,
  "title": "learn Flask",
  "done": 0,
  "priority": 2
}
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
  "id": 1,
  "title": "learn Flask",
  "done": 0,
  "priority": 2
}
```

Status code:

```text
201 CREATED
```

The `id` can be different depending on the current database state.

After creating a task, the API returns the full created task object.

---

## Create Task Validation

### Required Fields

The request body must contain:

```text
title
done
priority
```

If one of these fields is missing, the API returns a specific validation error.

Missing `title`:

```json
{
  "error": "title is required"
}
```

Missing `done`:

```json
{
  "error": "done is required"
}
```

Missing `priority`:

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

### Title Validation

The `title` value must be a non-empty string.

Invalid example:

```json
{
  "title": "",
  "done": 0,
  "priority": 2
}
```

Invalid example:

```json
{
  "title": "   ",
  "done": 0,
  "priority": 2
}
```

Response:

```json
{
  "error": "title must be a non-empty string"
}
```

Status code:

```text
400 BAD REQUEST
```

The `title` value must be 100 characters or less.

If `title` is longer than 100 characters:

```json
{
  "error": "title must be 100 characters or less"
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

## Update Task Title

### Request

```http
PATCH /api/tasks/title/1
Content-Type: application/json
```

### Body

```json
{
  "title": "new title"
}
```

### Response

```json
{
  "id": 1,
  "title": "new title",
  "done": 0,
  "priority": 2
}
```

Status code:

```text
200 OK
```

---

### Required Field

The request body must contain:

```text
title
```

If `title` is missing:

```json
{
  "error": "title is required"
}
```

Status code:

```text
400 BAD REQUEST
```

---

### Title Validation

The `title` value must be a non-empty string.

If `title` is empty or contains only spaces:

```json
{
  "error": "title must be a non-empty string"
}
```

Status code:

```text
400 BAD REQUEST
```

The `title` value must be 100 characters or less.

If `title` is longer than 100 characters:

```json
{
  "error": "title must be 100 characters or less"
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
{
  "id": 1,
  "title": "learn Flask",
  "done": 1,
  "priority": 2
}
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
{
  "id": 1,
  "title": "learn Flask",
  "done": 0,
  "priority": 1
}
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
  "id": 1,
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
- reading query parameters
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
- filtering tasks by `done`
- filtering tasks by `priority`
- counting task statistics
- grouping tasks by priority
- converting SQLite rows into JSON-friendly dictionaries
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
→ app.py validates title, done, and priority
→ app.py calls create_task(title, done, priority)
→ db.py inserts the task into SQLite
→ SQLite creates a new id
→ db.py returns the new id
→ app.py gets the created task by id
→ app.py returns JSON response with the created task object
```

---

### Getting All Tasks

```text
Client sends GET /api/tasks
→ Flask route is called
→ app.py reads the done and priority query parameters
→ both query parameters are None
→ app.py calls get_tasks(done, priority)
→ db.py reads all rows from SQLite
→ db.py converts each row into a task object
→ db.py returns a list of task objects
→ app.py returns the list as JSON
```

---

### Filtering Tasks

```text
Client sends GET /api/tasks with optional query parameters
→ Flask route is called
→ app.py reads the done and priority query parameters
→ app.py validates done if it exists
→ app.py validates priority if it exists
→ app.py converts query values from strings to integers
→ app.py calls get_tasks(done, priority)
→ db.py selects rows using the provided filters
→ db.py converts rows into task objects
→ app.py returns the list as JSON
```

Examples:

```text
GET /api/tasks
→ returns all tasks

GET /api/tasks?done=0
→ returns tasks where done = 0

GET /api/tasks?priority=2
→ returns tasks where priority = 2

GET /api/tasks?done=0&priority=2
→ returns tasks where done = 0 and priority = 2
```

---

### Getting Task Statistics

```text
Client sends GET /api/tasks/stats
→ Flask route is called
→ app.py calls get_task_stats()
→ db.py counts all tasks
→ db.py counts done tasks
→ db.py counts not_done tasks
→ db.py groups tasks by priority
→ db.py creates a statistics dictionary
→ app.py returns the dictionary as JSON
```

The `by_priority` field always contains priority keys `1`, `2`, and `3`.

If there are no tasks for a priority, its value is `0`.

---

### Getting One Task

```text
Client sends GET /api/tasks/<id>
→ Flask route is called
→ app.py calls get_task_by_id(task_id)
→ db.py reads one row from SQLite
→ if the row exists, db.py converts it into a task object
→ app.py returns the task object as JSON
```

If the task does not exist:

```text
db.py returns None
→ app.py returns 404 NOT FOUND
```

---

### Updating Task Title

```text
Client sends PATCH /api/tasks/title/<id>
→ Flask receives JSON body
→ app.py checks and validates title
→ app.py calls update_task_title(task_id, title)
→ db.py updates the task title in SQLite
→ app.py gets the updated task
→ app.py returns the updated task object as JSON
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
→ app.py returns the updated task object as JSON
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
→ app.py returns the updated task object as JSON
```

---

### Deleting a Task

```text
Client sends DELETE /api/tasks/<id>
→ Flask route is called
→ app.py calls delete_task_by_id(task_id)
→ db.py deletes the task from SQLite
→ app.py returns success message with deleted task id
```

---

# Current Response Format

Tasks are returned as JSON objects:

```json
{
  "id": 1,
  "title": "learn Flask",
  "done": 0,
  "priority": 2
}
```

A list of tasks is returned as an array of objects:

```json
[
  {
    "id": 1,
    "title": "learn Flask",
    "done": 0,
    "priority": 2
  }
]
```

The order of JSON object keys can differ depending on the client or framework settings. The important part is that the response contains the correct keys and values.

---

# Notes

This is a learning project.

It focuses on:

- Flask routes
- SQLite basics
- CRUD operations
- query parameters
- JSON request and response
- HTTP status codes
- request validation
- separating API logic from database logic
- converting database rows into clean API responses

This project does not include:

- user authentication
- frontend interface
- automated tests
- deployment configuration
- production database setup

---

# Possible Improvements

Future improvements:

- Add pagination
- Add automated tests
- Add Docker support later
- Add deployment instructions later

---

# Status

Current version:

- Basic CRUD works
- SQLite database works
- Flask routes work
- Request validation for `title` works
- Request validation for `done` works
- Request validation for `priority` works
- Separate database layer exists
- Tasks are returned as JSON objects
- Task `title` update route works
- Query filter by `done` works
- Query filter by `priority` works
- Main routes were manually checked
- Project is ready for GitHub upload as a learning backend project
- `POST /api/tasks` returns the created task object
- Combined query filters work
- Title length validation works
- Validation logic was moved into separate helper functions
- `GET /api/tasks/stats` works
- Task statistics are returned as JSON
- Tasks are counted by total, done, not_done, and priority
