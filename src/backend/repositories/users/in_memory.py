from src.backend.models.users import UserData
from src.backend.repositories.users.interface import UserRepository


class InMemoryUserRepository(UserRepository):
    def __init__(self) -> None:
        self.users: dict[str, UserData] = {}

    def create_user(self, username: str, password: str, email: str) -> UserData:
        raise NotImplementedError

    def get_user(self, id: int) -> UserData:
        raise NotImplementedError

    def get_users(self, start_id: int, end_id: int) -> list[UserData]:
        raise NotImplementedError

    def update_user(self, id: int, username: str | None, email: str | None) -> UserData:
        raise NotImplementedError

    def delete_user(self, id: int) -> None:
        raise NotImplementedError
