from fastapi import APIRouter

from src.models.tasks import (
    TaskPriority,
    TaskStatus,
    GetTaskResponse,
    GetTasksResponse,
    PostTaskResponse,
    PatchTaskResponse,
)

router = APIRouter()


@router.get("/tasks", tags=["tasks"])
async def get_tasks() -> GetTasksResponse:
    raise NotImplementedError


@router.get("/tasks/{id}", tags=["tasks"])
async def get_task(id: int) -> GetTaskResponse:
    raise NotImplementedError


@router.post("/tasks", tags=["tasks"])
async def create_task(
    name: str, description: str, priority: str, status: str
) -> PostTaskResponse:
    raise NotImplementedError


@router.patch("/tasks/{id}", tags=["tasks"])
async def update_task(
    id: int,
    name: str | None,
    description: str | None,
    status: TaskStatus | None,
    priority: TaskPriority | None,
) -> PatchTaskResponse:
    raise NotImplementedError


@router.delete("/tasks/{id}", tags=["tasks"])
async def delete_task(id: int) -> None:
    raise NotImplementedError
