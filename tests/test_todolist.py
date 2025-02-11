from app.models.models import Task, ToDoList, Status
import pytest

task = Task('GYM', 'Leg Day')
todo_list = ToDoList()


# Task tests
def test_create_task():
    assert task.title == 'GYM'
    assert task.desc == 'Leg Day'
    assert task.status == Status.ToDo


def test_edit_task():
    task.edit_task('Gym', 'Chest Day', Status.InProgress)
    assert task.title == 'Gym'
    assert task.desc == 'Chest Day'


def test_change_status_task():
    task.change_task_status(Status.Done)
    assert task.status == Status.Done


def test_show_task():
    assert task.show_task() == 'GYM - Leg Day - ToDo'


# ToDoList tests
def test_add_task():
    todo_list.add_task('Work', 'Create Report')
    assert len(todo_list.task_list) == 1
    assert todo_list.task_list[0].title == 'Work'
    assert todo_list.task_list[0].desc == 'Create Report'


def test_delete_task():
    todo_list.add_task('Grocery', 'Buy rice, milk and vegetables')
    index = 0
    deleted_task = todo_list.delete_task(index)
    assert len(todo_list.task_list) == 0
    assert deleted_task.title == 'Grocery'


def test_delete_incorrect_task():
    todo_list.add_task('Tickets', 'Reserve tickets for show')
    created_task_index = 0
    incorrect_index = 5
    deleted_task = todo_list.delete_task(incorrect_index)
    assert todo_list.task_list[created_task_index].title == 'Tickets'
    assert todo_list.task_list[created_task_index].desc == 'Reserve tickets for show'
    assert deleted_task is None
    assert len(todo_list.task_list) == 1


def test_show_todo_list_task():
    todo_list.add_task('Meeting', 'Meeting with co-workers at 6pm')
    task_index = 0
    assert todo_list.show_task(task_index) == 'Meeting - Meeting with co-workers at 6pm - ToDo'


def test_clear_todolist():
    todo_list.add_task('Task #1', 'First task')
    todo_list.add_task('Task #2', 'Second task')
    todo_list.clear_todo_list()
    assert len(todo_list.task_list) == 0

