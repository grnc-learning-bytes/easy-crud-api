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


class User(BaseModel):
    username: str
    email: str
    created_at: dt.datetime
    updated_at: dt.datetime


class UserData(BaseModel):
    id: int
    type: str = "user"
    attributes: User


############
# Get User #
############


class GetUserResponse(BaseModel):
    data: UserData
    meta: GetSingleMeta = GetSingleMeta()
    links: GetSingleLinks


##############
# List users #
##############


class GetUsersResponse(BaseModel):
    data: list[UserData]
    meta: GetManyMeta
    links: GetManyLinks


######################
# Post user response #
######################


class PostUserResponse(BaseModel):
    data: UserData
    meta: PostMeta
    links: PostLinks


#######################
# Patch user response #
#######################


class PatchUserResponse(BaseModel):
    data: UserData
    meta: PatchMeta
