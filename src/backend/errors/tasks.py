from fastapi import HTTPException


class TaskDoesNotExist(HTTPException):
    def __init__(self, headers: dict[str, str] | None = None):
        super().__init__(
            status_code=404,
            detail={
                "code": "task_does_not_exist",
                "description": "Task does not exist.",
            },
            headers=headers,
        )
