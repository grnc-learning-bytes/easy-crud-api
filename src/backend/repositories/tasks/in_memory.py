from src.backend.models.domain.tasks import Task
from src.backend.models.internal.tasks import TaskInternal
from src.backend.repositories.tasks.interface import TaskRepo


class InMemoryTaskRepo(TaskRepo):

    def __init__(self):
        pass

    def create_task(self, task: Task) -> TaskInternal:
        raise NotImplementedError
