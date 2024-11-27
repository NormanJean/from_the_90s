import sqlite3
from datetime import date
from create_db  import create_db


class Task:
    def __init__(self):
        with sqlite3.connect("todo_db.db") as self.conn:
            self.cursor = self.conn.cursor()

    def add_task(self, name, description, deadline, priority, status):
        self.cursor.execute("""INSERT INTO tasks (
                            name, description, deadline, priority, status) 
                            VALUES (?, ?, ?, ?, ?)""",
                            (name, description, deadline, priority, status)
                            )
        self.conn.commit()

    def del_task(self, name):
        self.cursor.execute("DELETE FROM tasks WHERE name = ?", (name,))
        self.conn.commit()

    # def get_completed(self):
    #     self.cursor.execute("SELECT deadline, name, description, priority, status FROM tasks WHERE status = ?", (True,))
    #
    #
    # def get_overdue(self):
    #     self.cursor.execute('SELECT deadline, name, description, priority, status FROM tasks WHERE status = ?', (None,))
    # def check(self):
    #     d = date.today
    #     self.cursor.execute("SELECT deadline FROM tasks WHERE deadline < ?", (d))

    def update_task(self, new_name, new_description, new_deadline, new_priority, name):
        self.cursor.execute("UPDATE tasks SET name = ?, description = ?, deadline = ?, priority = ? WHERE name = ?", (new_name, new_description, new_deadline, new_priority, name))
        self.conn.commit()

    def update_status(self, name, new_status):
        self.cursor.execute("UPDATE tasks SET status = ? WHERE name = ?",(new_status, name))
        self.conn.commit()

    def get_all(self):
        self.cursor.execute("SELECT deadline, name, description, priority, status FROM tasks;")
        for all_tasks in self.cursor.fetchall():
            tasks = {'Deadline:  ': all_tasks[0]}
            tasks['Задача:    '] = all_tasks[1]
            tasks['Описание:  '] = all_tasks[2]
            tasks['Приоритет: '] = all_tasks[3]
            if all_tasks[4] == 1:
                tasks['Статус:    '] = 'Выполнено'
            else:
                tasks['Статус:    '] = 'Не выполнено'
            for fields in tasks.items():
                print(*fields)
            print()


    def sort_by(self, by):
        self.cursor.execute("SELECT deadline, name, description, priority, status FROM tasks;")
        q = sorted(self.cursor.fetchall(), key=lambda x: x[by])
        for all_tasks in q:
            tasks = {'Deadline:  ': all_tasks[0]}
            tasks['Задача:    '] = all_tasks[1]
            tasks['Описание:  '] = all_tasks[2]
            tasks['Приоритет: '] = all_tasks[3]
            if all_tasks[4] == 1:
                tasks['Статус:    '] = 'Выполнено'
            else:
                tasks['Статус:    '] = 'Не выполнено'
            for fields in tasks.items():
                print(*fields)
            print()


    # def filter_by(self, by):
    #     self.cursor.execute("""SELECT deadline, name, description, priority, status
    #                         FROM tasks WHERE deadline == ?;""", (by)
    #                         )
    #     for all_tasks in self.cursor.fetchall():
    #         tasks = {'Deadline:  ': all_tasks[0]}
    #         tasks['Задача:    '] = all_tasks[1]
    #         tasks['Описание:  '] = all_tasks[2]
    #         tasks['Приоритет: '] = all_tasks[3]
    #         if all_tasks[4] == 1:
    #             tasks['Статус:    '] = 'Выполнено'
    #         else:
    #             tasks['Статус:    '] = 'Не выполнено'
    #         for fields in tasks.items():
    #             print(*fields)
    #         print()

    def find_by(self, by):
        self.cursor.execute("""SELECT deadline, name, description, priority, status 
                            FROM tasks WHERE name == ? OR description == ?;""",
                            (by, by)
                            )
        for all_tasks in self.cursor.fetchall():
            tasks = {'Deadline:  ': all_tasks[0]}
            tasks['Задача:    '] = all_tasks[1]
            tasks['Описание:  '] = all_tasks[2]
            tasks['Приоритет: '] = all_tasks[3]
            if all_tasks[4] == 1:
                tasks['Статус:    '] = 'Выполнено'
            elif all_tasks[4] == 0:
                tasks['Статус:    '] = 'Не выполнено'
            else:
                tasks['Статус:    '] = 'Просрочено'
            for fields in tasks.items():
                print(*fields)
            print()


if __name__ == '__main__':
    create_db()
    task = Task()
    print('Ваши задачи:')
    print()
    # task.check()
    task.get_all()

    start = 'да'
    while start == 'да':
        print('Желаете добавить новые задачи? ')
        start = input('да/нет: ')
        if start == 'да':
            name = input('Задача: ')
            description = input('Описание задачи: ')
            deadline = input('Выполнить до (ГГГГ-ММ-ДД): ')
            # while deadline ==
            # if deadline == None:
            #     print('Необходимо указать срок выполнения: ')
            try:
                priority = int(input('Приоритет задачи: '))
            except:
                priority = 3

            while priority > 5 or priority < 1:
                try:
                    priority = int(input('Укажите число в диапазоне < 1 - 5 >: '))
                except:
                    priority = 3

            status = False

            task.add_task(name, description, deadline, priority, status)
        # task.update_status('Погладить кошку', True)
        # task.update_task('Допилить программу', '', '2024-11-28', '', 'Сдать проект на отлично')
        # task.get_unfulfilled()
        # task.del_completed()
        else:
            print()


'''
Название задачи не должно повторяться в том случае, если у них один дэдлайн
по нескольким задачам может быть один дэдлайн
задачи могут иметь одно название

дэдлайн можно двигать, если текущая дата не наступила

фильтровать по выполненым, по датам, по просроченным
статус просрочено наступает если время выполнения < дэдлайна

Ставить звездочку на выполненных задачах
В фильтрах предложить смотреть выполненные и просроченные

Добавить обновление статуса просрочки
'''


