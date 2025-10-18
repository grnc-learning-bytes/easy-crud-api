from fastapi import APIRouter

from src.backend.models.users import (
    GetUserResponse,
    GetUsersResponse,
    PostUserResponse,
    PatchUserResponse,
)

router = APIRouter()


@router.get("/users", tags=["users"])
async def get_users() -> GetUsersResponse:
    raise NotImplementedError


@router.get("/users/me", tags=["users"])
async def get_user_me() -> GetUserResponse:
    raise NotImplementedError


@router.get("/users/{id}", tags=["users"])
async def get_user(id: int) -> GetUserResponse:
    raise NotImplementedError


@router.post("/users", tags=["users"])
async def create_user(username: str, password: str, email: str) -> PostUserResponse:
    raise NotImplementedError


@router.patch("/users/{id}", tags=["users"])
async def patch_user(
    id: int, username: str | None, email: str | None
) -> PatchUserResponse:
    raise NotImplementedError


@router.delete("/users/{id}", tags=["users"])
async def delete_user(id: int) -> None:
    raise NotImplementedError
