import datetime as dt

from src.backend.errors.tasks import TaskDoesNotExist
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
        self._tasks[store_task.id] = store_task
        return store_task

    def get_task(self, id: int) -> TaskInternal:
        task = self._tasks.get(id, None)
        if task is None:
            raise TaskDoesNotExist
        return task

    def update_task(self, id: int, task: Task) -> None:
        cur_task = self._tasks.get(id, None)
        if cur_task is None:
            raise TaskDoesNotExist
        self._tasks[id] = TaskInternal(
            id=self._id,
            attributes=TaskInternalAttributes(
                name=task.name,
                description=task.description,
                priority=task.priority,
                status=task.status,
                tags=task.tags,
                created_at=cur_task.attributes.created_at,
                updated_at=dt.datetime.now(dt.timezone.utc),
            ),
        )

    def list_tasks(
        self, page: int, page_size: int, tags: set[str] | None = None
    ) -> list[TaskInternal]:
        if tags is None:
            tags = set[str]()

        # Task filtering
        def is_task_properly_tagged(t: TaskInternal) -> bool:
            task_tags = set[str]() if t.attributes.tags is None else t.attributes.tags
            cond = any([tag in task_tags for tag in tags])
            print("Task tags:", task_tags)
            print("Tags:", tags)
            print("Contains:", cond)
            print()
            return cond

        relevant_tasks = [
            t for _, t in self._tasks.items() if is_task_properly_tagged(t)
        ]

        # Pagination
        start_idx: int = (page - 1) * page_size
        end_idx: int = start_idx + page_size
        return relevant_tasks[start_idx:end_idx]

    def delete_task(self, id: int) -> None:
        task = self._tasks.pop(id, None)
        if task is None:
            raise TaskDoesNotExist()
