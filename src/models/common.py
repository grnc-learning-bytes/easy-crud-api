from pydantic import BaseModel

############
# Metadata #
############


class GetSingleMeta(BaseModel):
    pass


class GetManyMeta(BaseModel):
    total: int
    page: int
    page_size: int


class PostMeta(BaseModel):
    created: bool


class PatchMeta(BaseModel):
    updated: bool


#########
# Links #
#########


class GetSingleLinks(BaseModel):
    self: str


class GetManyLinks(BaseModel):
    self: str
    next: str


class PostLinks(BaseModel):
    self: str
