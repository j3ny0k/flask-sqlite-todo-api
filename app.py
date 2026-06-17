from flask import Flask, jsonify, request
from db import (
    init_db,
    create_task,
    get_all_tasks,
    get_task_by_id,
    update_task_title,
    update_task_done,
    update_task_priority,
    delete_task_by_id,
    delete_all_tasks,
)

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify({"message": "Flask is working"}), 200


@app.post("/api/tasks")
def api_create_task():
    data = request.get_json()

    if not data or "title" not in data or "done" not in data or "priority" not in data:
        return jsonify({"error": "title, done and priority are required"}), 400

    title = data["title"]

    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "title must be a non-empty string"}), 400

    done = data["done"]
    priority = data["priority"]

    if done not in [0, 1]:
        return jsonify({"error": "done must be 0 or 1"}), 400

    if priority not in [1, 2, 3]:
        return jsonify({"error": "priority must be 1, 2 or 3"}), 400

    task_id = create_task(title, done, priority)

    return jsonify({"id": task_id}), 201


@app.get("/api/tasks")
def api_get_tasks():
    tasks = get_all_tasks()
    return jsonify(tasks), 200


@app.get("/api/tasks/<int:task_id>")
def api_get_task_by_id(task_id):
    task = get_task_by_id(task_id)

    if task is None:
        return jsonify({"error": "task not found"}), 404

    return jsonify(task), 200


@app.patch("/api/tasks/title/<int:task_id>")
def api_update_task_title(task_id):
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "title is required"}), 400

    title = data["title"]

    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "title must be a non-empty string"}), 400

    updated_count = update_task_title(task_id, title)

    if updated_count == 0:
        return jsonify({"error": "task not found"}), 404

    task = get_task_by_id(task_id)
    return jsonify(task), 200


@app.patch("/api/tasks/done/<int:task_id>")
def api_update_task_done(task_id):
    data = request.get_json()

    if not data or "done" not in data:
        return jsonify({"error": "done is required"}), 400

    done = data["done"]

    if done not in [0, 1]:
        return jsonify({"error": "done must be 0 or 1"}), 400

    updated_count = update_task_done(task_id, done)

    if updated_count == 0:
        return jsonify({"error": "task not found"}), 404

    task = get_task_by_id(task_id)
    return jsonify(task), 200


@app.patch("/api/tasks/priority/<int:task_id>")
def api_update_task_priority(task_id):
    data = request.get_json()

    if not data or "priority" not in data:
        return jsonify({"error": "priority is required"}), 400

    priority = data["priority"]

    if priority not in [1, 2, 3]:
        return jsonify({"error": "priority must be 1, 2 or 3"}), 400

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

    return jsonify({"message": "task deleted"}), 200


@app.delete("/api/tasks")
def api_delete_all_tasks():
    deleted_count = delete_all_tasks()
    return jsonify({"deleted": deleted_count}), 200


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
