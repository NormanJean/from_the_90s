import sqlite3

class CreateDB:
    def __init__(self):
        with sqlite3.connect("../todo_db.db") as self.conn:
            self.cursor = self.conn.cursor()
            try:
                self.cursor.execute(
                    """
                    CREATE TABLE tasks (
                    id integer PRIMARY KEY AUTOINCREMENT,
                    name varchar(64) NOT NULL,
                    description text,
                    deadline text NOT NULL,  
                    priority integer DEFAULT 3,
                    status integer DEFAULT 0 
                    )
                """
                )
            except:
                pass

if __name__ == '__main__':
    create_db = CreateDB()
