from enum import Enum
from pydantic import BaseModel


class TaskPriority(Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    MINOR = "minor"


class TaskStatus(Enum):
    BACKLOG = "backlog"
    READY = "ready"
    IN_PROGRESS = "in_progress"
    VALIDATING = "validating"
    DONE = "done"


class Task(BaseModel):
    name: str
    description: str
    priority: TaskPriority
    status: TaskStatus
    tags: set[str] | None = None
