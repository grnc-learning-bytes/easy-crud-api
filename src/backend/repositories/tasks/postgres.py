from src.backend.repositories.tasks.interface import TaskRepo, Task, TaskInternal
from src.backend.settings.settings import PostgresSettings


class PostgresTaskRepo(TaskRepo):

    def __init__(self, settings: PostgresSettings):
        self._settings = settings

    def create_task(self, task: Task) -> TaskInternal:
        raise NotImplementedError

    def get_task(self, id: int) -> TaskInternal:
        raise NotImplementedError

    def update_task(self, id: int, task: Task) -> None:
        raise NotImplementedError

    def list_tasks(
        self, page: int, page_size: int, tags: set[str] | None = None
    ) -> list[TaskInternal]:
        raise NotImplementedError

    def delete_task(self, id: int) -> None:
        raise NotImplementedError
