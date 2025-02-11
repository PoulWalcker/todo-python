from models.models import Status, Task, ToDoList
import argparse

todo_list = ToDoList()


def add_task(args):
    """Show task from todo_list by id"""
    todo_list.add_task(args.title, args.description)
    print(f"Task '{args.title}' added successfully!")


def show_tasks(args):
    """Show list of tasks from todo_list"""
    todo_list.show_all_tasks()


def show_task(args):
    """Show from todo_list"""
    todo_list.show_task(args.id)


def complete_task(args):
    """Complete task from todo_list"""
    if 0 <= args.id < len(todo_list.task_list):
        todo_list.task_list[args.id].change_task_status(Status.Done)
        print(f"Task #{args.id} marked as done.")
    else:
        print("Invalid task id.")


def delete_task(args):
    """Delete task from todo_list"""
    deleted_task = todo_list.delete_task(args.id)
    if deleted_task:
        print(f"Task {args.id} deleted.")
    else:
        print("Invalid task id.")


def clear_todo_list(args):
    """Clear todo_list"""
    todo_list.clear_todo_list()
    print("All tasks removed.")


def main():
    parser = argparse.ArgumentParser(description="ToDo List CLI")
    subparsers = parser.add_subparsers()

    # add task
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("title", type=str, help="Task title")
    parser_add.add_argument("description", type=str, help="Task description")
    parser_add.set_defaults(func=add_task)

    # show all tasks
    parser_show_all = subparsers.add_parser("show_all", help="Show all tasks")
    parser_show_all.set_defaults(func=show_tasks)

    # show one task
    parser_show = subparsers.add_parser("show", help="Show task by ID")
    parser_show.add_argument("id", type=int, help="Task ID")
    parser_show.set_defaults(func=show_task)

    # complete task
    parser_complete = subparsers.add_parser("complete", help="Mark task as done")
    parser_complete.add_argument("id", type=int, help="Task ID")
    parser_complete.set_defaults(func=complete_task)

    # delete task
    parser_delete = subparsers.add_parser("delete", help="Delete task by ID")
    parser_delete.add_argument("id", type=int, help="Task ID")
    parser_delete.set_defaults(func=delete_task)

    # clear completed tasks
    parser_clear = subparsers.add_parser("clear", help="Remove all completed tasks")
    parser_clear.set_defaults(func=clear_todo_list)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
