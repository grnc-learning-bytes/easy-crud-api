from fastapi import APIRouter

from src.backend.models.tasks import (
    TaskPriority,
    TaskStatus,
    GetTaskResponse,
    GetTasksResponse,
    PostTaskResponse,
    PatchTaskResponse,
)

router = APIRouter()


@router.get("/tasks", tags=["tasks"])
async def get_tasks(tags: list[str]) -> GetTasksResponse:
    raise NotImplementedError


@router.get("/tasks/{id}", tags=["tasks"])
async def get_task(id: int) -> GetTaskResponse:
    raise NotImplementedError


@router.post("/tasks", tags=["tasks"])
async def create_task(
    name: str,
    description: str,
    priority: str,
    status: str,
    tags: list[str] | None = None,
) -> PostTaskResponse:
    raise NotImplementedError


@router.patch("/tasks/{id}", tags=["tasks"])
async def update_task(
    id: int,
    name: str | None = None,
    description: str | None = None,
    status: TaskStatus | None = None,
    priority: TaskPriority | None = None,
    tags: list[str] | None = None,
) -> PatchTaskResponse:
    raise NotImplementedError


@router.delete("/tasks/{id}", tags=["tasks"])
async def delete_task(id: int) -> None:
    raise NotImplementedError
