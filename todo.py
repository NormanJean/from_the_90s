import sqlite3
import create_db


class Task:
    def __init__(self, name = '', description = '', deadline = '', priority = 3, status = False):
            with sqlite3.connect("todo_db.db") as self.conn:
                self.cursor = self.conn.cursor()
            self.name = name
            self.description = description
            self.deadline = deadline
            self.priority = priority
            self.status = status

class Scheduler:
    def __init__(self):
        with sqlite3.connect("todo_db.db") as self.conn:
            self.cursor = self.conn.cursor()

    def add_task(self):
        pass

    def del_task(self):
        pass

    def rename_task(self):
        pass

    def update_description(self):
        pass

    def update_deadline(self):
        pass

    def update_priority(self):
        pass

    def update_status(self):
        pass

    def get_unfulfilled(self):
        pass

    def update_status(self):
        pass

    def sort_by(self):
        pass

    def filter_by(self):
        pass

    def find_by(self):
        pass


if __name__ == '__main__':
    create_db.create_db()
    task = Task()
    scheduler = Scheduler()


