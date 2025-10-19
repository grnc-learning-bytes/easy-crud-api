from abc import ABC, abstractmethod

from src.backend.models.domain.tasks import Task
from src.backend.models.internal.tasks import TaskInternal


class TaskRepo(ABC):
    @abstractmethod
    def create_task(self, task: Task) -> TaskInternal:
        raise NotImplementedError
