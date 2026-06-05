from enum import StrEnum
from datetime import datetime
from abc import abstractmethod, ABC


class Status(StrEnum):
    todo = "todo"
    in_progress = "in-progress"
    complete = "done"


class ITask(ABC):

    @abstractmethod
    def update_description(self):
        raise NotImplementedError

    @abstractmethod
    def mark_done(self):
        raise NotImplementedError

    @abstractmethod
    def mark_picked(self):
        raise NotImplementedError


class Task(ITask):
    def __init__(self, unique_id: int, description: str):
        self.__dict__["status"] = Status.todo
        self.__dict__["id"] = unique_id
        self.__dict__["description"] = description
        self.__dict__["created_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__dict__["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def update_description(self, new_description):
        self.description = new_description

    def mark_done(self):
        self.status = Status.complete

    def mark_picked(self):
        self.status = Status.in_progress

    def __setattr__(self, name, value):
        if getattr(self, name, None) != value:
            self.on_change(name, value)
            if name != "updated_at":
                self.__dict__["updated_at"] = datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
        super().__setattr__(name, value)

    def on_change(self, name, value):
        print(f"🔔 '{name}' changed to '{value}'!")

    def __str__(self):
        task = {
            "id": self.id,
            "description": self.description,
            "updated_at": self.updated_at,
            "created_at": self.created_at,
            "status": self.status,
        }
        return str(task)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "updated_at": self.updated_at,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        instance = cls.__new__(cls)

        instance.__dict__["id"] = data["id"]
        instance.__dict__["description"] = data["description"]
        instance.__dict__["status"] = Status(data["status"])
        instance.__dict__["updated_at"] = data["updated_at"]
        instance.__dict__["created_at"] = data["created_at"]

        return instance
