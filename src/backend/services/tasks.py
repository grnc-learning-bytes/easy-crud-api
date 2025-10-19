from src.backend.models.domain.tasks import Task
from src.backend.models.responses.tasks import CreateTaskResponse, TaskResponseLinks
from src.backend.repositories.tasks.interface import TaskRepo


class TaskService:
    def __init__(self, task_repo: TaskRepo):
        self._task_repo = task_repo

    def create_task(self, task: Task) -> CreateTaskResponse:
        task_internal = self._task_repo.create_task(task)
        task_response_data = task_internal.to_task_response_data()
        return CreateTaskResponse(
            data=task_response_data,
            links=TaskResponseLinks()
        )
