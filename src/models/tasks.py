import datetime as dt
from enum import Enum
from pydantic import BaseModel

from src.models.common import (
    GetManyMeta,
    GetManyLinks,
    GetSingleMeta,
    GetSingleLinks,
    PostMeta,
    PostLinks,
    PatchMeta,
)

#################
# Relationships #
#################


class TaskRelationshipUser(BaseModel):
    type: str = "user"
    id: int


class TaskRelationshipData(BaseModel):
    data: TaskRelationshipUser


class TaskRelationships(BaseModel):
    user: TaskRelationshipData


########################
# Task data attributes #
########################


class TaskPriority(Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    MINOR = "minor"


class TaskStatus(Enum):
    BACKLOG = "backlog"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class Task(BaseModel):
    name: str
    description: str
    priority: TaskPriority
    status: TaskStatus
    tags: list[str] | None = None
    created_at: dt.datetime
    updated_at: dt.datetime


class TaskData(BaseModel):
    id: int
    type: str = "task"
    attributes: Task
    relationships: TaskRelationships


#############
# Responses #
#############


class GetTaskResponse(BaseModel):
    data: TaskData
    meta: GetSingleMeta = GetSingleMeta()
    links: GetSingleLinks


class GetTasksResponse(BaseModel):
    data: list[TaskData]
    meta: GetManyMeta
    links: GetManyLinks


class PostTaskResponse(BaseModel):
    data: TaskData
    meta: PostMeta
    links: PostLinks


class PatchTaskResponse(BaseModel):
    data: TaskData
    meta: PatchMeta
