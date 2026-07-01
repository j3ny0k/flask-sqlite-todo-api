import sqlite3


def row_to_task(row):
    return {
        "id": row[0],
        "title": row[1],
        "done": row[2],
        "priority": row[3],
    }


DB_NAME = "tasks.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        done INTEGER NOT NULL DEFAULT 0,
        priority INTEGER NOT NULL DEFAULT 2
    )
    """)

    conn.commit()
    conn.close()


def create_task(title, done, priority):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO tasks (title, done, priority)
        VALUES (?, ?, ?)
        """,
        (title, done, priority),
    )

    conn.commit()
    task_id = cursor.lastrowid
    conn.close()

    return task_id


def get_tasks(done, priority):
    conn = get_connection()
    cursor = conn.cursor()

    sql = "SELECT id, title, done, priority FROM tasks"
    conditions = []
    params = []

    if done is not None:
        conditions.append("done = ?")
        params.append(done)

    if priority is not None:
        conditions.append("priority = ?")
        params.append(priority)

    if conditions:
        sql += " WHERE "
        sql += " AND ".join(conditions)

    sql += " ORDER BY id DESC"

    cursor.execute(sql, params)

    rows = cursor.fetchall()

    tasks = [row_to_task(row) for row in rows]

    conn.close()
    return tasks


def get_task_stats():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM tasks")
    all_rows = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM tasks WHERE done = 1")
    rows_done = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM tasks WHERE done = 0")
    rows_undone = cursor.fetchone()[0]

    cursor.execute(
        "SELECT priority, COUNT(*) FROM tasks GROUP BY priority ORDER BY priority"
    )
    rows_by_priority = cursor.fetchall()

    by_priority = {"1": 0, "2": 0, "3": 0}

    for field in rows_by_priority:
        priority = field[0]
        count = field[1]

        by_priority[str(priority)] = count

    response = {
        "total": all_rows,
        "done": rows_done,
        "not_done": rows_undone,
        "by_priority": by_priority,
    }

    conn.close()
    return response


def get_task_by_id(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, title, done, priority FROM tasks WHERE id = ?", (task_id,)
    )

    row = cursor.fetchone()

    conn.close()

    if row is None:
        return None

    return row_to_task(row)


def update_task_title(task_id, title):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE tasks SET title = ? WHERE id = ?", (title, task_id))

    updated_count = cursor.rowcount

    conn.commit()
    conn.close()

    return updated_count


def update_task_done(task_id, done):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE tasks SET done = ? WHERE id = ?", (done, task_id))

    updated_count = cursor.rowcount

    conn.commit()
    conn.close()

    return updated_count


def update_task_priority(task_id, priority):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE tasks SET priority = ? WHERE id = ?", (priority, task_id))

    updated_count = cursor.rowcount

    conn.commit()
    conn.close()

    return updated_count


def delete_task_by_id(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    deleted_count = cursor.rowcount

    conn.commit()
    conn.close()

    return deleted_count


def delete_all_tasks():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks")
    deleted_count = cursor.rowcount

    cursor.execute("DELETE FROM sqlite_sequence WHERE name = ?", ("tasks",))

    conn.commit()
    conn.close()

    return deleted_count


if __name__ == "__main__":
    init_db()
