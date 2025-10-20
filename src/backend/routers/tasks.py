from fastapi import APIRouter, Query, Depends
from typing import Annotated

from src.backend.models.domain.tasks import Task
from src.backend.models.responses.tasks import (
    ListTasksResponse,
    GetTaskResponse,
    CreateTaskResponse,
)
from src.backend.settings.container import Container, DepsContainer


router = APIRouter()


@router.get("/tasks", tags=["tasks"])
async def list_tasks(
    container: Annotated[DepsContainer, Depends(Container.container)], page: int, tags: Annotated[set[str] | None, Query()] = None,
) -> ListTasksResponse:
    print(tags)
    return container.task_service().list_tasks(page, tags)


@router.get("/tasks/{id}", tags=["tasks"])
async def get_task(container: Annotated[DepsContainer, Depends(Container.container)], id: int) -> GetTaskResponse:
    return container.task_service().get_task(id)


@router.post("/tasks", tags=["tasks"], status_code=201)
async def create_task(container: Annotated[DepsContainer, Depends(Container.container)], task: Task) -> CreateTaskResponse:
    return container.task_service().create_task(task)


@router.put("/tasks/{id}", tags=["tasks"], status_code=204)
async def update_task(container: Annotated[DepsContainer, Depends(Container.container)], id: int, task: Task) -> None:
    container.task_service().update_task(id, task)


@router.delete("/tasks/{id}", tags=["tasks"])
async def delete_task(container: Annotated[DepsContainer, Depends(Container.container)], id: int) -> None:
    container.task_service().delete_task(id)
