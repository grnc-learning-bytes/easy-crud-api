from fastapi import APIRouter, Query
from typing import Annotated

from src.backend.models.domain.tasks import Task
from src.backend.models.responses.tasks import (
    ListTasksResponse,
    GetTaskResponse,
    CreateTaskResponse,
)
from src.backend.settings.container import Container

container = Container.container()
task_service = container.task_service()
router = APIRouter()


@router.get("/tasks", tags=["tasks"])
async def list_tasks(
    page: int, tags: Annotated[set[str] | None, Query()] = None
) -> ListTasksResponse:
    print(tags)
    return task_service.list_tasks(page, tags)


@router.get("/tasks/{id}", tags=["tasks"])
async def get_task(id: int) -> GetTaskResponse:
    return task_service.get_task(id)


@router.post("/tasks", tags=["tasks"], status_code=201)
async def create_task(task: Task) -> CreateTaskResponse:
    return task_service.create_task(task)


@router.put("/tasks/{id}", tags=["tasks"], status_code=204)
async def update_task(id: int, task: Task) -> None:
    task_service.update_task(id, task)


@router.delete("/tasks/{id}", tags=["tasks"])
async def delete_task(id: int) -> None:
    task_service.delete_task(id)
