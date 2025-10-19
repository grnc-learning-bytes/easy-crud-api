from src.backend.models.domain.tasks import Task
from src.backend.models.responses.tasks import CreateTaskResponse, ListTasksResponse
from src.backend.repositories.tasks.interface import TaskRepo


class TaskService:
    page_size: int = 10

    def __init__(self, task_repo: TaskRepo):
        self._task_repo = task_repo

    def create_task(self, task: Task) -> CreateTaskResponse:
        task_internal = self._task_repo.create_task(task)
        task_response_data = task_internal.to_task_response_data()
        return CreateTaskResponse(data=task_response_data)

    def list_tasks(self, page: int, tags: set[str] | None = None) -> ListTasksResponse:
        tasks_internal = self._task_repo.list_tasks(
            page=page,
            page_size=self.page_size,
            tags=tags,
        )
        tasks_response_data = [t.to_task_response_data() for t in tasks_internal]
        return ListTasksResponse(data=tasks_response_data)
    
    def delete_task(self, id: int) -> None:
        self._task_repo.delete_task(id)
