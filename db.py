import sqlite3

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


def get_all_tasks():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, title, done, priority FROM tasks ORDER BY id DESC")
    rows = cursor.fetchall()

    conn.close()
    return rows


def get_task_by_id(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, title, done, priority FROM tasks WHERE id = ?", (task_id,)
    )

    row = cursor.fetchone()

    conn.close()
    return row


def update_task_done(task_id, done):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE tasks SET done = ? WHERE id = ?", (done, task_id))

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
