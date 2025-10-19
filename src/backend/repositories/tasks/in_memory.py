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

    def list_tasks(
        self, page: int, page_size: int, tags: set[str] | None = None
    ) -> list[TaskInternal]:
        if tags is None:
            tags = set[str]()

        # Task filtering
        def is_task_properly_tagged(t: TaskInternal) -> bool:
            task_tags = set[str]() if t.attributes.tags is None else t.attributes.tags
            return any([t in task_tags for t in tags])

        relevant_tasks = [
            t for _, t in self._tasks.items() if is_task_properly_tagged(t)
        ]

        # Pagination
        start_idx: int = (page - 1) * page_size
        end_idx: int = start_idx + page_size
        return relevant_tasks[start_idx:end_idx]
