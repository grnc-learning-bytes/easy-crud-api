"""
Structure of task responses follows the JSON API specification:

GET /tasks
{
    "data": [
        {
            "id": 1,
            "attributes": [
                {...},
                {...},
            ],
            "relationships": [],
            "links": {}
        }
    ],
    "metadata": {},
    "links": {
        "self": "...",
        "next": "...",
        "prev": "...",
    }
}
"""

import datetime as dt
from pydantic import BaseModel, HttpUrl

from src.backend.models.domain.tasks import Task

######################
# Task Response Data #
######################


class TaskResponseAttributes(Task):
    created_at: dt.datetime
    updated_at: dt.datetime


class TaskResponseData(BaseModel):
    id: int
    attributes: TaskResponseAttributes
    relationships: list | None = None
    links: dict | None = None


############################
# Metadata Response Models #
############################


class TaskResponseLinks(BaseModel):
    self: HttpUrl | None = None
    prev: HttpUrl | None = None
    next: HttpUrl | None = None


#########################
# Tasks Response Models #
#########################


class ListTasksResponse(BaseModel):
    data: list[TaskResponseData]
    metadata: dict | None = None
    links: TaskResponseLinks = TaskResponseLinks()


class GetTaskResponse(BaseModel):
    data: TaskResponseData
    metadata: dict | None = None
    links: TaskResponseLinks = TaskResponseLinks()


class CreateTaskResponse(BaseModel):
    data: TaskResponseData
    metadata: dict | None = None
    links: TaskResponseLinks = TaskResponseLinks()


class UpdateTaskResponse(BaseModel):
    data: TaskResponseData
    metadata: dict | None = None
    links: TaskResponseLinks = TaskResponseLinks()
