import datetime as dt
from sqlalchemy import MetaData, Column, Integer, String, Enum, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base

from src.backend.models.domain.tasks import TaskStatus, TaskPriority


metadata_obj = MetaData()
Base = declarative_base(metadata=metadata_obj)

###########
# Helpers #
###########

def now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)

##############
# ORM models #
##############

# Define ORM models
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    status = Column(Enum(TaskStatus), nullable=False)
    priority = Column(Enum(TaskPriority), nullable=False)
    created_at = Column(DateTime, default=now, nullable=False)
    updated_at = Column(DateTime, default=now, onupdate=now, nullable=False)


class TaskTag(Base):
    __tablename__ = "task_tags"

    id = Column(Integer, primary_key=True, nullable=False)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)
    created_at = Column(DateTime, default=now, nullable=False)
    updated_at = Column(DateTime, default=now, onupdate=now, nullable=False)
