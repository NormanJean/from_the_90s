import sqlite3


def create_db():
    with sqlite3.connect("tests/todo_db.db") as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                """
                CREATE TABLE tasks (
                id integer PRIMARY KEY AUTOINCREMENT,
                name text NOT NULL,
                description text,
                deadline text NOT NULL,
                priority integer DEFAULT 3,
                status integer DEFAULT 0)
                """
            )
        except:
            pass


if __name__ == "__main__":
    create_db()
