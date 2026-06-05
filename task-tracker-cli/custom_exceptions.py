class TaskManagerException(Exception):
    pass


class DataLoadingError(TaskManagerException):
    pass


class FileEmptyError(TaskManagerException):
    pass


class TaskNotFound(TaskManagerException):
    pass


class DataManipulationException(TaskManagerException):
    pass


class TaskCreationError(DataManipulationException):
    pass


class TaskUpdateError(DataManipulationException):
    pass


class InvalidStatus(TaskUpdateError):
    pass
