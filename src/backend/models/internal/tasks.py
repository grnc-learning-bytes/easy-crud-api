from src.backend.models.responses.tasks import TaskResponseData, TaskResponseAttributes


class TaskInternalAttributes(TaskResponseAttributes):
    def to_task_response_attributes(self) -> TaskResponseAttributes:
        return TaskResponseAttributes(
            name=self.name,
            description=self.description,
            priority=self.priority,
            status=self.status,
            tags=self.tags,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )


class TaskInternal(TaskResponseData):
    attributes: TaskInternalAttributes

    def to_task_response_data(self) -> TaskResponseData:
        return TaskResponseData(
            id=self.id,
            attributes=self.attributes.to_task_response_attributes(),
            relationships=self.relationships,
            links=self.links,
        )
