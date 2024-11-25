import sqlite3

def create_database():
    connection = sqlite3.connect("todo_db.db")
    cursor = connection.cursor()
    try:
        cursor.execute(
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
    connection.commit()
    connection.close()


if __name__ == '__main__':
    create_database()