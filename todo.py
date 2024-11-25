import sqlite3
from create_db  import create_db


class Task:
    def __init__(self, name = '', description = '', deadline = '', priority = 3, status = None):
            with sqlite3.connect("todo_db.db") as self.conn:
                self.cursor = self.conn.cursor()
            self.name = name
            self.description = description
            self.deadline = deadline
            self.priority = priority
            self.status = status

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
    create_db()
    task = Task()

'''
Название задачи не должно повторяться в том случае, если у них один дэдлайн
по нескольким задачам может быть один дэдлайн
задачи могут иметь одно название
дэдлайн можно двигать, если текущая дата не наступила
приоритет от 1-5
отправка уведомлений на почту
фильтровать по выполненым, по датам, по просроченным

'''