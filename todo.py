import sqlite3
from asyncio import all_tasks
from os.path import split

from create_db  import create_db


class Task:
    def __init__(self):
        with sqlite3.connect("todo_db.db") as self.conn:
            self.cursor = self.conn.cursor()

    def add_task(self, name, description, deadline, priority, status):
        self.cursor.execute("""INSERT INTO tasks (
                            name, description, deadline, priority, status) 
                            VALUES (?, ?, ?, ?, ?)""",
                            (name, description, deadline, priority, status))
        self.conn.commit()

    def del_task(self, name):
        self.cursor.execute(f'DELETE FROM tasks WHERE name = ?', (name,))
        self.conn.commit()

    def del_completed(self):
        self.cursor.execute(f'DELETE FROM tasks WHERE status = ?', (True,))
        self.conn.commit()

    def update_task(self, new_name, new_description, new_deadline, new_priority, name):
        self.cursor.execute("UPDATE tasks SET name = ?, description = ?, deadline = ?, priority = ? WHERE name = ?", (new_name, new_description, new_deadline, new_priority, name))
        self.conn.commit()

    def update_status(self, name, new_status):
        self.cursor.execute('UPDATE tasks SET status = ? WHERE name = ?',(new_status, name))
        self.conn.commit()

    def get_unfulfilled(self):
        self.cursor.execute("SELECT * FROM tasks WHERE status = 0")
        print(self.cursor.fetchall())

    def get_all(self):
        self.cursor.execute("SELECT name, description, deadline, priority, status FROM tasks;")
        for all_tasks in self.cursor.fetchall():
            a = {'Задача': all_tasks[0]}
            a['Описание'] = all_tasks[1]
            print(a)




    def sort_by(self, by):

        pass

    def filter_by(self):
        pass

    def find_by(self):
        pass


if __name__ == '__main__':
    create_db()
    task = Task()
    # # print('Просмотреть имеющиеся задачи?')
    # # show = input('да/нет: ')
    # name = input('Задача: ')
    # description = input('Описание задачи: ')
    # deadline = input('Выполнить до: ')
    # # while deadline ==
    # # if deadline == None:
    # #     print('Необходимо указать срок выполнения: ')
    # try:
    #     priority = int(input('Приоритет задачи: '))
    # except:
    #     priority = 3
    #
    # while priority > 5 or priority < 1:
    #     try:
    #         priority = int(input('Укажите число в диапазоне < 1 - 5 >: '))
    #     except:
    #         priority = 3
    #
    # status = False
    # task.add_task(name, description, deadline, priority, status)
    # task.update_status('qwqwe', True)
    # task.update_task('Допилить программу', '', '2024-11-28', '', 'Сдать проект на отлично')
    # task.get_unfulfilled()
    task.get_all()
    # task.del_completed()


'''

Название задачи не должно повторяться в том случае, если у них один дэдлайн
по нескольким задачам может быть один дэдлайн
задачи могут иметь одно название
дэдлайн можно двигать, если текущая дата не наступила
приоритет от 1-5
фильтровать по выполненым, по датам, по просроченным
статус просрочено наступает если время выполнения < дэдлайна
'''


