from task_manager import TaskManager
from custom_exceptions import *
from task import Status

task_manager = TaskManager()


def add_task(description: str):
    try:
        created, task_id = task_manager.create_new_task(description)
        if created:
            print(f"Task successfully created :: task_id :: {task_id}")
        else:
            print(f"Failure in creating a new task")
    except Exception as e:
        print(f"Exception while creating a task")


def update_task(task_id: int, description: str):
    try:
        task_manager.update_task_description(task_id, description)
    except TaskNotFound:
        print(f"No task found with id: {task_id}")
    except Exception as e:
        print(f"TaskUpdateFailure: {e}")


def delete_task(task_id):
    try:
        task_manager.delete_task(task_id)
    except TaskNotFound:
        print(f"No task found with id: {task_id}")
    except Exception as e:
        print(f"TaskDeleteFailure: {e}")


def mark_status(task_id, status):
    try:
        task_manager.update_task_status(task_id, status)
    except TaskNotFound:
        print(f"No task found with id: {task_id}")
    except Exception as e:
        print(f"TaskUpdateFailure: {e}")


def get_task_status(task_id):
    try:
        status = task_manager.get_status(task_id)
        print(f"status recieved for task_id {task_id} : {status}")
    except TaskNotFound:
        print(f"No task found with id: {task_id}")
    except Exception as e:
        print(f"CheckTaskStatusFailure: {e}")


def list_all_tasks():
    try:
        task_manager.list_all_tasks()
    except FileEmptyError:
        print('Database is still empty: let"s add something shall we??')
    except Exception as e:
        print(f"FetchError: {e}")


def list_task_by_status(status):
    try:
        task_manager.list_task_by_status(status)
    except TaskNotFound:
        print(f"No task found with status : {status}")
    except Exception as e:
        print(f"FetchByStatusError: {e}")
