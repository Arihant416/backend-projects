import json
from task import Task, Status
from custom_exceptions import *


filename = "data.json"


class TaskManager:
    def __init__(self):
        self.last_known_index = 0
        self.registry = {}
        self.load_all_tasks_in_memory()

    def load_all_tasks_in_memory(self):
        try:
            with open(filename, "r") as f:
                task_list = json.load(f)
                if task_list:
                    for task in task_list:
                        task_id = int(task["id"])
                        self.registry[task_id] = Task.from_dict(task)
                        self.last_known_index = max(task_id, self.last_known_index)
        except FileNotFoundError:
            print(f"database does not exists; fresh json-file will be created")
        except Exception as e:
            print(f"Exception in task load {e}")
            self.registry = {}

    def save_tasks_to_file(self):
        serialized_tasks = [task.to_dict() for task in self.registry.values()]
        with open(filename, "w") as file:
            json.dump(serialized_tasks, file, indent=4)

    def get_index(self):
        self.last_known_index += 1
        return self.last_known_index

    def create_new_task(self, description: str):
        try:
            task_id = self.get_index()
            print(f"Creating new task -> index_allocated :: {task_id}")
            task = Task(task_id, description)
            self.registry[task_id] = task
            return True, task_id
        except Exception as e:
            print(f"Exception in creating a new task {e}")
            return False, None

    def list_all_tasks(self):
        if self.registry:
            for task in self.registry.values():
                print(task, type(task))
            return
        raise FileEmptyError

    def get_task_by_id(self, task_id: int):
        if task_id in self.registry:
            return self.registry[task_id]
        raise TaskNotFound

    def list_task_by_status(self, status: str):
        result = [task for task in self.registry.values() if task.status == status]
        if result:
            for task in result:
                print(task)
            return
        raise TaskNotFound

    def update_task_status(self, task_id: int, status: Status):
        if task_id in self.registry:
            self.registry[task_id].status = status
            return
        raise TaskNotFound

    def update_task_description(self, task_id: int, new_description: str):
        if task_id in self.registry:
            self.registry[task_id].description = new_description
            return
        raise TaskNotFound

    def delete_task(self, task_id):
        if task_id not in self.registry:
            raise TaskNotFound
        del self.registry[task_id]
        print(f"Successfully deleted task with id {task_id}")

    def get_status(self, task_id):
        if task_id not in self.registry:
            raise TaskNotFound
        return self.registry[task_id].status.value
