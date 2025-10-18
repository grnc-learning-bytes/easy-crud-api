from fastapi import HTTPException


class UserAlreadyExists(HTTPException):
    def __init__(self, headers):
        super().__init__(
            status_code=404,
            detail={"error": "user_already_exists", "detail": "User already exists."},
            headers=headers,
        )


class UserDoesNotExist(HTTPException):
    def __init__(self, headers):
        super().__init__(
            status_code=404, detail="User does not exist.", headers=headers
        )
