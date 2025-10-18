from abc import ABC, abstractmethod

from src.backend.models.users import UserData


class UserRepository(ABC):

    @abstractmethod
    def create_user(self, username: str, password: str, email: str) -> UserData:
        raise NotImplementedError

    @abstractmethod
    def get_user(self, id: int) -> UserData:
        raise NotImplementedError

    @abstractmethod
    def get_users(self, start_id: int, end_id: int) -> list[UserData]:
        raise NotImplementedError

    @abstractmethod
    def update_user(self, id: int, username: str | None, email: str | None) -> UserData:
        raise NotImplementedError
    
    @abstractmethod
    def delete_user(self, id: int) -> None:
        raise NotImplementedError
