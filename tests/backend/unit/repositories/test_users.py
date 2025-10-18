import pytest

from src.backend.settings.container import Container
from src.backend.repositories.users.interface import UserRepository


@pytest.fixture
def user_repo(faker_container: Container) -> UserRepository:
    return faker_container.user_repo()


def test_can_create_user(user_repo: UserRepository):
    user_repo.create_user(
        username="Bob", password="I-love-tools", email="bob.builder@constructor.com"
    )


def test_can_update_user(user_repo: UserRepository):
    pass


def test_cant_update_missing_user(user_repo: UserRepository):
    pass


def test_can_delete_user(user_repo: UserRepository):
    pass


def test_cant_delete_missing_user(user_repo: UserRepository):
    pass
