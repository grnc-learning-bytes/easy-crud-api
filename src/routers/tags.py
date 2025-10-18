from fastapi import APIRouter

from src.models.tags import (
    GetTagResponse,
    GetTagsResponse,
    PostTagResponse,
    PatchTagResponse,
)

router = APIRouter()


@router.get("/tags", tags=["tags"])
async def get_tags() -> GetTagsResponse:
    raise NotImplementedError


@router.get("/tags/{id}", tags=["tags"])
async def get_tag(id: int) -> GetTagResponse:
    raise NotImplementedError


@router.post("/tags", tags=["tags"])
async def create_tag(name: str, description: str) -> PostTagResponse:
    raise NotImplementedError


@router.patch("/tags/{id}", tags=["tags"])
async def update_tag(
    id: int, name: str | None, description: str | None
) -> PatchTagResponse:
    raise NotImplementedError


@router.delete("/tags/{id}", tags=["tags"])
async def delete_tag(id: int) -> None:
    raise NotImplementedError
