from src.backend.models.domain.tasks import Task
from src.backend.models.responses.tasks import (
    ListTasksResponse,
    GetTaskResponse,
    CreateTaskResponse,
    UpdateTaskResponse,
)
from src.backend.settings.container import Container

from fastapi import APIRouter

container = Container.container()
task_service = container.task_service()
router = APIRouter()


@router.get("/tasks", tags=["tasks"])
async def list_tasks(page: int, tags: set[str] | None = None) -> ListTasksResponse:
    return task_service.list_tasks(page, tags)


@router.get("/tasks/{id}", tags=["tasks"])
async def get_task(id: int) -> GetTaskResponse:
    return task_service.get_task(id)


@router.post("/tasks", tags=["tasks"], status_code=201)
async def create_task(task: Task) -> CreateTaskResponse:
    return task_service.create_task(task)


@router.put("/tasks/{id}", tags=["tasks"])
async def update_task(id: int, task: Task) -> UpdateTaskResponse:
    raise NotImplementedError


@router.delete("/tasks/{id}", tags=["tasks"])
async def delete_task(id: int) -> None:
    task_service.delete_task(id)
