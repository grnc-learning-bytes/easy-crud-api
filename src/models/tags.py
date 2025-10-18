import datetime as dt
from pydantic import BaseModel

from src.models.common import (
    GetManyLinks,
    GetManyMeta,
    GetSingleLinks,
    GetSingleMeta,
    PostLinks,
    PostMeta,
    PatchMeta,
)

#################
# Relationships #
#################


class TagRelationshipUser(BaseModel):
    type: str = "user"
    id: int


class TagRelationshipsData(BaseModel):
    data: TagRelationshipUser


class TagRelationships(BaseModel):
    user: TagRelationshipsData


##############
# Data Model #
##############


class Tag(BaseModel):
    name: str
    description: str
    created_at: dt.datetime
    updated_at: dt.datetime


class TagData(BaseModel):
    id: int
    type: str = "tag"
    attributes: Tag
    relationships: TagRelationships


#############
# Responses #
#############


class GetTagResponse(BaseModel):
    data: TagData
    meta: GetSingleMeta = GetSingleMeta()
    links: GetSingleLinks


class GetTagsResponse(BaseModel):
    data: list[TagData]
    meta: GetManyMeta
    links: GetManyLinks


class PostTagResponse(BaseModel):
    data: TagData
    meta: PostMeta
    links: PostLinks


class PatchTagResponse(BaseModel):
    data: TagData
    meta: PatchMeta
