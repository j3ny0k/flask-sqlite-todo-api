from flask import Flask, jsonify, request
from db import (
    init_db,
    create_task,
    get_tasks,
    get_task_stats,
    get_task_by_id,
    update_task_title,
    update_task_done,
    update_task_priority,
    delete_task_by_id,
    delete_all_tasks,
)

app = Flask(__name__)


def is_validation_error(result):
    return isinstance(result, tuple)


def get_required_field(data, field):
    if not data or field not in data:
        return jsonify({"error": f"{field} is required"}), 400

    result = data[field]

    return result


def validate_title(data):
    title = get_required_field(data, "title")

    if is_validation_error(title):
        return title

    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "title must be a non-empty string"}), 400

    title = title.strip()

    if len(title) > 100:
        return jsonify({"error": "title must be 100 characters or less"}), 400

    return title


def validate_done(data):
    done = get_required_field(data, "done")

    if is_validation_error(done):
        return done

    if done not in [0, 1]:
        return jsonify({"error": "done must be 0 or 1"}), 400

    return done


def validate_priority(data):
    priority = get_required_field(data, "priority")

    if is_validation_error(priority):
        return priority

    if priority not in [1, 2, 3]:
        return jsonify({"error": "priority must be 1, 2 or 3"}), 400

    return priority


@app.get("/")
def home():
    return jsonify({"message": "Flask is working"}), 200


@app.post("/api/tasks")
def api_create_task():
    data = request.get_json()

    result = validate_title(data)

    if not isinstance(result, str):
        return result

    title = result

    result = validate_done(data)

    if not isinstance(result, int):
        return result

    done = result

    result = validate_priority(data)

    if not isinstance(result, int):
        return result

    priority = result

    task_id = create_task(title, done, priority)
    task = get_task_by_id(task_id)

    return jsonify(task), 201


@app.get("/api/tasks")
def api_get_tasks():
    done = request.args.get("done")
    priority = request.args.get("priority")

    if done is not None:
        if done not in ["0", "1"]:
            return jsonify({"error": "done must be 0 or 1"}), 400

        done = int(done)

    if priority is not None:
        if priority not in ["1", "2", "3"]:
            return jsonify({"error": "priority must be 1, 2 or 3"}), 400

        priority = int(priority)

    tasks = get_tasks(done, priority)
    return jsonify(tasks), 200


@app.get("/api/tasks/<int:task_id>")
def api_get_task_by_id(task_id):
    task = get_task_by_id(task_id)

    if task is None:
        return jsonify({"error": "task not found"}), 404

    return jsonify(task), 200


@app.get("/api/tasks/stats")
def api_get_task_stats():
    return get_task_stats(), 200


@app.patch("/api/tasks/title/<int:task_id>")
def api_update_task_title(task_id):
    data = request.get_json()

    result = validate_title(data)

    if not isinstance(result, str):
        return result

    title = result

    updated_count = update_task_title(task_id, title)

    if updated_count == 0:
        return jsonify({"error": "task not found"}), 404

    task = get_task_by_id(task_id)
    return jsonify(task), 200


@app.patch("/api/tasks/done/<int:task_id>")
def api_update_task_done(task_id):
    data = request.get_json()

    result = validate_done(data)

    if not isinstance(result, int):
        return result

    done = result

    updated_count = update_task_done(task_id, done)

    if updated_count == 0:
        return jsonify({"error": "task not found"}), 404

    task = get_task_by_id(task_id)
    return jsonify(task), 200


@app.patch("/api/tasks/priority/<int:task_id>")
def api_update_task_priority(task_id):
    data = request.get_json()

    result = validate_priority(data)

    if not isinstance(result, int):
        return result

    priority = result

    updated_count = update_task_priority(task_id, priority)

    if updated_count == 0:
        return jsonify({"error": "task not found"}), 404

    task = get_task_by_id(task_id)
    return jsonify(task), 200


@app.delete("/api/tasks/<int:task_id>")
def api_delete_task_by_id(task_id):
    deleted_count = delete_task_by_id(task_id)

    if deleted_count == 0:
        return jsonify({"error": "task not found"}), 404

    return jsonify({"message": "task deleted", "id": task_id}), 200


@app.delete("/api/tasks")
def api_delete_all_tasks():
    deleted_count = delete_all_tasks()
    return jsonify({"deleted": deleted_count}), 200


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
