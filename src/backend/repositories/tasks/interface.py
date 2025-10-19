from abc import ABC, abstractmethod

from src.backend.models.domain.tasks import Task
from src.backend.models.internal.tasks import TaskInternal


class TaskRepo(ABC):
    @abstractmethod
    def create_task(self, task: Task) -> TaskInternal:
        raise NotImplementedError

    @abstractmethod
    def get_task(self, id: int) -> TaskInternal:
        raise NotImplementedError

    @abstractmethod
    def update_task(self, id: int, task: Task) -> None:
        raise NotImplementedError

    @abstractmethod
    def list_tasks(
        self, page: int, page_size: int, tags: set[str] | None = None
    ) -> list[TaskInternal]:
        raise NotImplementedError

    @abstractmethod
    def delete_task(self, id: int) -> None:
        raise NotImplementedError
