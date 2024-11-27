import sqlite3
from datetime import date
from create_db  import create_db


class Task:
    def __init__(self):
        with sqlite3.connect("todo_db.db") as self.conn:
            self.cursor = self.conn.cursor()

    def check(self, date):
        self.cursor.execute("UPDATE tasks SET status = NULL WHERE deadline < ? AND status == 0", (str(date),))
        self.conn.commit()

    def get_all(self):
        self.cursor.execute("SELECT deadline, name, description, priority, status, id FROM tasks;")
        for all_tasks in self.cursor.fetchall():
            tasks = {'Deadline:  ': all_tasks[0]}
            tasks['Задача:    '] = all_tasks[1]
            tasks['Описание:  '] = all_tasks[2]
            tasks['Приоритет: '] = all_tasks[3]
            if all_tasks[4] == 1:
                tasks['Статус:    '] = '[*]'
            elif all_tasks[4] == 0:
                tasks['Статус:    '] = '[ ]'
            else:
                tasks['Статус:    '] = '[!]'
            tasks['id:        '] = all_tasks[5]
            for fields in tasks.items():
                print(*fields)
            print()

    def add_task(self, name, description, deadline, priority, status):
        self.cursor.execute("""INSERT INTO tasks (
                            name, description, deadline, priority, status) 
                            VALUES (?, ?, ?, ?, ?)""",
                            (name, description, deadline, priority, status)
                            )
        self.conn.commit()

    def update_task(self, new_name, new_description, new_deadline, new_priority, id):
        self.cursor.execute("UPDATE tasks SET id = ?, description = ?, deadline = ?, priority = ? WHERE name = ?", (new_name, new_description, new_deadline, new_priority, id))
        self.conn.commit()

    def del_task(self, id):
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", (id,))
        self.conn.commit()

    def sort_by(self, by):
        self.cursor.execute("SELECT deadline, name, description, priority, status, id FROM tasks;")
        q = sorted(self.cursor.fetchall(), key=lambda x: x[by])
        for all_tasks in q:
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
            tasks['id:        '] = all_tasks[5]
            for fields in tasks.items():
                print(*fields)
            print()

    def filter_by(self, by):
        self.cursor.execute("""SELECT deadline, name, description, priority, status, id
                            FROM tasks WHERE deadline == ?;""", (by,)
                            )
        for all_tasks in self.cursor.fetchall():
            tasks = {'Deadline:  ': all_tasks[0]}
            tasks['Задача:    '] = all_tasks[1]
            tasks['Описание:  '] = all_tasks[2]
            tasks['Приоритет: '] = all_tasks[3]
            if all_tasks[4] == 1:
                tasks['Статус:    '] = '[*]'
            elif all_tasks[4] == 0:
                tasks['Статус:    '] = '[ ]'
            else:
                tasks['Статус:    '] = '[!]'
            tasks['id:        '] = all_tasks[5]
            for fields in tasks.items():
                print(*fields)
            print()

    def get_completed(self):
        self.cursor.execute("SELECT deadline, name, description, priority, status, id FROM tasks WHERE status = ?", (True,))
        for all_tasks in self.cursor.fetchall():
            tasks = {'Deadline:  ': all_tasks[0]}
            tasks['Задача:    '] = all_tasks[1]
            tasks['Описание:  '] = all_tasks[2]
            tasks['Приоритет: '] = all_tasks[3]
            if all_tasks[4] == 1:
                tasks['Статус:    '] = '[*]'
            elif all_tasks[4] == 0:
                tasks['Статус:    '] = '[ ]'
            else:
                tasks['Статус:    '] = '[!]'
            tasks['id:        '] = all_tasks[5]
            for fields in tasks.items():
                print(*fields)
            print()

    def get_overdue(self):
        self.cursor.execute('SELECT deadline, name, description, priority, status, id FROM tasks WHERE status IS NULL')
        for all_tasks in self.cursor.fetchall():
            tasks = {'Deadline:  ': all_tasks[0]}
            tasks['Задача:    '] = all_tasks[1]
            tasks['Описание:  '] = all_tasks[2]
            tasks['Приоритет: '] = all_tasks[3]
            if all_tasks[4] == 1:
                tasks['Статус:    '] = '[*]'
            elif all_tasks[4] == 0:
                tasks['Статус:    '] = '[ ]'
            else:
                tasks['Статус:    '] = '[!]'
            tasks['id:        '] = all_tasks[5]
            for fields in tasks.items():
                print(*fields)
            print()


    def find_by(self, by):
        self.cursor.execute("""SELECT deadline, name, description, priority, status, id
                            FROM tasks WHERE name == ? OR id == ?;""",
                            (by, by)
                            )
        for all_tasks in self.cursor.fetchall():
            tasks = {'Deadline:  ': all_tasks[0]}
            tasks['Задача:    '] = all_tasks[1]
            tasks['Описание:  '] = all_tasks[2]
            tasks['Приоритет: '] = all_tasks[3]
            if all_tasks[4] == 1:
                tasks['Статус:    '] = '[*]'
            elif all_tasks[4] == 0:
                tasks['Статус:    '] = '[ ]'
            else:
                tasks['Статус:    '] = '[!]'
            tasks['id:        '] = all_tasks[5]
            for fields in tasks.items():
                print(*fields)
            print()

    def update_status(self, new_status, id):
        self.cursor.execute("UPDATE tasks SET status = ? WHERE id = ?",(new_status, id))
        self.conn.commit()


if __name__ == '__main__':
    create_db()
    task = Task()
    task.check(date.today())
    todo = 1
    while todo != 0:
        print('Главное меню >>>>>')
        print('')
        print('Выберите действие:')
        print('------------------')
        print('1 - Мои задачи', '2 - Добавить задачу', '3 - Обновить задачу',
              '4 - Удалить задачу', '5 - Отсортировать', '6 - Отфильтровать',
              '7 - Найти',   sep='\n')
        print('------------------')
        print('0 - Завершить','\n')

        action = input('Ввод 0 - 7: ')
        match action:
            case '1':
                print()
                print('Ваши задачи:')
                task.get_all()
            case '2':
                start = 'да'
                while start == 'да':
                    name = input('Задача: ')
                    description = input('Описание задачи: ')
                    deadline = input('Выполнить до (ГГГГ-ММ-ДД): ')
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
                    print('Добавить новую задачу? ')
                    start = input('да/нет: ')
                    if start == 'да':
                        task.add_task(name, description, deadline, priority, status)
                        break
                else:
                    break

            case '3':
                start = 'да'
                while start == 'да':
                    id = input('ID задачи для изменения: ')
                    name = input('Задача: ')
                    description = input('Описание задачи: ')
                    deadline = input('Выполнить до (ГГГГ-ММ-ДД): ')
                    try:
                        priority = int(input('Приоритет задачи: '))
                    except:
                        priority = 3

                    while priority > 5 or priority < 1:
                        try:
                            priority = int(input('Укажите число в диапазоне < 1 - 5 >: '))
                        except:
                            priority = 3
                    print('Обновить задачу? ')
                    start = input('да/нет: ')
                    if start == 'да':
                        task.update_task(name, description, deadline, priority, id)
                        break
                    else:
                        break

            case '4':
                start = 'да'
                while start == 'да':
                    id = input('ID задачи для удаления: ')
                    print('Удалить задачу? ')
                    start = input('да/нет: ')
                    if start == 'да':
                        task.del_task(id)
                        break
                    else:
                        break

            case '5':
                checks = True
                while checks is True:
                    try:
                        by = input('Сортировка по: ')
                        match by:
                            case 'Deadline':
                                by = 0
                            case 'Задача':
                                by = 1
                            case 'Описание':
                                by = 2
                            case 'Приоритет':
                                by = 3
                            case 'Статус':
                                by = 4
                            case 'id':
                                by = 5
                        task.sort_by(by)
                        checks = False
                    except:
                        checks = True
                        print('Введите наименование поля')

            case '6':
                print('Фильтры:')
                print('1 - По крайней дате')
                print('2 - По выполненным')
                print('3 - По просроченным', '\n')
                filter = input('Выберите фильтр 1-3: ')
                try:
                    if filter == '1':
                        by = input('Введите число (ГГГГ-ММ-ДД): ')
                        task.filter_by(by)
                        print()
                    elif filter == '2':
                        task.get_completed()
                    else:
                        task.get_overdue()
                except Exception as ex:
                    print(type(ex))

            case '7':
                by = input('Найти (id OR name): ')
                task.find_by(by)
                print('Поставить флаг выполнения? [*]')
                # a = input(f'[{input()}]')
                flag = input()
                if flag == '*':
                    task.update_status(1, by)
            case '0':
                break
