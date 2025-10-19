from src.backend.models.domain.tasks import Task
from src.backend.models.responses.tasks import (
    ListTasksResponse,
    GetTaskResponse,
    CreateTaskResponse,
    UpdateTaskResponse,
)

from fastapi import APIRouter

router = APIRouter()


@router.get("/tasks", tags=["tasks"])
async def list_tasks(tags: list[str] | None = None) -> ListTasksResponse:
    raise NotImplementedError


@router.get("/tasks/{id}", tags=["tasks"])
async def get_task(id: int) -> GetTaskResponse:
    raise NotImplementedError


@router.post("/tasks", tags=["tasks"])
async def create_task(task: Task) -> CreateTaskResponse:
    raise NotImplementedError


@router.put("/tasks/{id}", tags=["tasks"])
async def update_task(id: int, task: Task) -> UpdateTaskResponse:
    raise NotImplementedError


@router.delete("/tasks/{id}", tags=["tasks"])
async def delete_task(id: int) -> None:
    raise NotImplementedError
