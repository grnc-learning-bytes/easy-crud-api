from abc import ABC, abstractmethod

from src.backend.models.users import UserData, GetSingleMeta, GetManyMeta


class UserRepository(ABC):
    @abstractmethod
    def create_user(
        self, username: str, password: str, email: str
    ) -> tuple[UserData, GetSingleMeta]:
        raise NotImplementedError

    @abstractmethod
    def get_user(self, id: int) -> tuple[UserData, GetSingleMeta]:
        raise NotImplementedError

    @abstractmethod
    def get_users(
        self, page: int, page_size: int
    ) -> tuple[list[UserData], GetManyMeta]:
        raise NotImplementedError

    @abstractmethod
    def update_user(
        self, id: int, username: str | None = None, email: str | None = None
    ) -> tuple[UserData, GetSingleMeta]:
        raise NotImplementedError

    @abstractmethod
    def delete_user(self, id: int) -> None:
        raise NotImplementedError
