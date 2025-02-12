from enum import Enum
from typing import List
import json


class Status(Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class Task:
    def __init__(self, id: int, title: str, description: str, status: Status = Status.TODO):
        self.id = id
        self.title = title
        self.description = description
        self.status = status

    def to_dict(self):
        return {"id": self.id, "title": self.title, "description": self.description, "status": self.status.value}

    @staticmethod
    def from_dict(data):
        return Task(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            status=Status(data["status"])
        )

    def edit_task(self, title: str = None, desc: str = None, status: Status = None):
        if title:
            self.title = title
        if desc:
            self.description = desc
        if status:
            self.status = status

    def change_task_status(self, status: Status):
        self.status = status

    def show_task(self):
        return f"{self.title} - {self.description} - {self.status.name}"


class ToDoList:
    FILE_PATH = "tasks.json"

    def __init__(self, task_list: List[Task] = None):
        self.task_list = task_list or []
        self.load_from_file()

    def add_task(self, title: str, description: str, status: Status = Status.TODO):
        new_id = self.task_list[-1].id + 1 if self.task_list else 1
        task = Task(new_id, title, description, status)
        self.task_list.append(task)
        self.save_to_file()
        return task

    def delete_task(self, task_id: int):
        self.task_list = [task for task in self.task_list if task.id != task_id]
        self.save_to_file()

    def show_all_tasks(self):
        return "\n".join([f'{task.id} {task.title} - {task.status.value}' for task in self.task_list])

    def show_task(self, task_id: int):
        task = next((task for task in self.task_list if task.id == task_id), None)
        return f'{task.id} {task.title} - {task.status.value}' if task else 'Task not found'

    def complete_task(self, task_id: int):
        for task in self.task_list:
            if task.id == task_id:
                task.status = Status.DONE
                self.save_to_file()
                return
        print('Task not found')

    def clear_todo_list(self):
        self.task_list.clear()
        self.save_to_file()

    def save_to_file(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([Task.to_dict(task) for task in self.task_list], f, indent=4)

    def load_from_file(self):
        try:
            with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.task_list = [Task.from_dict(task) for task in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.task_list = []
