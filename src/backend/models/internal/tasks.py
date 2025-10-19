import datetime as dt

from src.backend.models.domain.tasks import Task


class TaskInternal(Task):
    created_at: dt.datetime
    updated_at: dt.datetime
