from src.backend.repositories.users.interface import (
    UserRepository,
    GetSingleMeta,
    GetManyMeta,
)
from src.backend.models.users import UserData
from src.backend.settings.settings import PgSettings


class PgUserRepository(UserRepository):
    def __init__(self, db_settings: PgSettings):
        raise NotImplementedError

    def create_user(
        self, username: str, password: str, email: str
    ) -> tuple[UserData, GetSingleMeta]:
        raise NotImplementedError

    def get_user(self, id: int) -> tuple[UserData, GetSingleMeta]:
        raise NotImplementedError

    def get_users(
        self, page: int, page_size: int
    ) -> tuple[list[UserData], GetManyMeta]:
        raise NotImplementedError

    def update_user(
        self, id: int, username: str | None = None, email: str | None = None
    ) -> tuple[UserData, GetSingleMeta]:
        raise NotImplementedError

    def delete_user(self, id: int) -> None:
        raise NotImplementedError
