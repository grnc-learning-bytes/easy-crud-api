import datetime as dt

from src.backend.models.domain.tasks import Task
from src.backend.models.internal.tasks import TaskInternal, TaskInternalAttributes
from src.backend.repositories.tasks.interface import TaskRepo


class InMemoryTaskRepo(TaskRepo):
    def __init__(self) -> None:
        self._id: int = 0
        self._tasks: dict[int, TaskInternal] = {}

    def create_task(self, task: Task) -> TaskInternal:
        now = dt.datetime.now(dt.timezone.utc)
        store_task = TaskInternal(
            id=self._id,
            attributes=TaskInternalAttributes(
                name=task.name,
                description=task.description,
                priority=task.priority,
                status=task.status,
                tags=task.tags,
                created_at=now,
                updated_at=now,
            ),
        )
        self._id += 1
        return store_task
