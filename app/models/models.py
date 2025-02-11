from enum import Enum
from typing import List


class Status(Enum):
    ToDo = 1
    InProgress = 2
    Done = 3


class Task:
    def __init__(self, title: str, desc: str, status: Status = Status.ToDo):
        self.title = title
        self.desc = desc
        self.status = status

    def edit_task(self, title: str = None, desc: str = None, status: Status = None):
        if title:
            self.title = title
        if desc:
            self.desc = desc
        if status:
            self.status = status

    def change_task_status(self, status: Status):
        self.status = status

    def show_task(self):
        return f'{self.title} - {self.desc} - {self.status.name}'


class ToDoList:

    def __init__(self, task_list: List[Task] = None):
        self.task_list = task_list or []

    def add_task(self, title: str, description: str, status: Status = Status.ToDo):
        task = Task(title, description, status)
        self.task_list.append(task)

    def delete_task(self, index: int):

        if 0 <= index < len(self.task_list):
            return self.task_list.pop(index)
        return None

    def show_all_tasks(self):
        for task in self.task_list:
            print(task.show_task())

    def show_task(self, index: int):
        if 0 <= index < len(self.task_list):
            return self.task_list[index].show_task()
        return 'Task is not found'

    def clear_todo_list(self):
        self.task_list.clear()
