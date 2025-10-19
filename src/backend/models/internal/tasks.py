from src.backend.models.responses.tasks import TaskResponseData


class TaskInternal(TaskResponseData):
    pass

    def to_task_response_data(self) -> TaskResponseData:
        return TaskResponseData(
            id=self.id,
            attributes=self.attributes,
            relationships=self.relationships,
            links=self.links,
        )
