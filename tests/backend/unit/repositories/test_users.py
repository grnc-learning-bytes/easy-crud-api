import faker
import pytest

from src.backend.settings.container import Container
from src.backend.repositories.users.errors import UserDoesNotExist, UserAlreadyExists
from src.backend.repositories.users.interface import UserRepository


############
# Fixtures #
############


@pytest.fixture
def user_repo(faker_container: Container) -> UserRepository:
    return faker_container.user_repo()


@pytest.fixture
def user_attributes() -> dict:
    return {
        "username": "Bob",
        "password": "I-love-tools",
        "email": "bob.builder@constructor.com",
    }


def random_user() -> dict:
    fake = faker.Faker()
    return {
        "username": fake.user_name(),
        "password": fake.password(),
        "email": fake.email(),
    }


def random_users(n_users: int) -> list[dict]:
    return [random_user() for _ in range(n_users)]


def random_user_pages(n_users: int, page_size: int) -> list[list[dict]]:
    user_pages: list[list[dict]] = []
    user_page: list[dict] = []
    for i in range(n_users):
        if i % page_size == 0:
            user_pages.append(user_page)
            user_page = []
        user_page.append(random_user())
    return user_pages


######################
# Test user creation #
######################


def test_can_create_user(user_repo: UserRepository, user_attributes: dict):
    user, _ = user_repo.create_user(**user_attributes)
    fetched_user, _ = user_repo.get_user(user.id)
    assert fetched_user == user


def test_cant_create_existing_user(user_repo: UserRepository, user_attributes: dict):
    user_repo.create_user(**user_attributes)
    with pytest.raises(UserAlreadyExists):
        user_repo.create_user(**user_attributes)


######################
# Test using listing #
######################


def test_list_empty(user_repo: UserRepository):
    users, _ = user_repo.get_users(1, 10)
    assert users == []


def test_returns_all_users(user_repo: UserRepository, user_attributes: dict):
    users = [user_repo.create_user(**user_attributes)[0] for _ in range(5)]
    fetched_users, _ = user_repo.get_users(1, 10)
    assert users == fetched_users


def test_users_are_paginated(user_repo: UserRepository):
    user_attrs = random_user_pages(28, 10)
    users = [[user_repo.create_user(**attrs)[0] for attrs in _u] for _u in user_attrs]
    assert (
        len(users) == 3
        and len(users[0]) == 10
        and len(users[1]) == 10
        and len(users[2]) == 8
    )
    fetched_users = [user_repo.get_users(i + 1, 10)[0] for i in range(3)]
    assert users == fetched_users


#####################
# Test user updates #
#####################


def test_empty_update_does_not_change_user(
    user_repo: UserRepository, user_attributes: dict
):
    user, _ = user_repo.create_user(**user_attributes)
    updated_user, _ = user_repo.update_user(user.id)
    assert updated_user == user


def test_can_update_user_name(user_repo: UserRepository, user_attributes: dict):
    user, _ = user_repo.create_user(**user_attributes)
    updated_user, _ = user_repo.update_user(user.id, username="Mark")
    assert user.attributes.username != updated_user.attributes.username
    updated_user.attributes.username = user.attributes.username
    assert user == updated_user


def test_can_update_user_email(user_repo: UserRepository, user_attributes: dict):
    user, _ = user_repo.create_user(**user_attributes)
    updated_user, _ = user_repo.update_user(user.id, email="mark@builders.com")
    assert user.attributes.email != updated_user.attributes.email
    updated_user.attributes.email = user.attributes.email
    assert user == updated_user


def test_can_update_name_and_email(user_repo: UserRepository, user_attributes: dict):
    user, _ = user_repo.create_user(**user_attributes)
    updated_user, _ = user_repo.update_user(
        user.id, username="Mark", email="mark@builders.com"
    )
    assert (
        user.attributes.username != updated_user.attributes.username
        and user.attributes.email != updated_user.attributes.email
    )
    updated_user.attributes.username = user.attributes.username
    updated_user.attributes.email = user.attributes.email
    assert user == updated_user


def test_cant_update_missing_user(user_repo: UserRepository):
    with pytest.raises(UserDoesNotExist):
        user_repo.update_user(1, "Mark")


######################
# Test user deletion #
######################


def test_can_delete_user(user_repo: UserRepository, user_attributes: dict):
    user, _ = user_repo.create_user(**user_attributes)
    user_repo.delete_user(user.id)
    with pytest.raises(UserDoesNotExist):
        user_repo.get_user(user.id)


def test_cant_delete_missing_user(user_repo: UserRepository):
    with pytest.raises(UserDoesNotExist):
        user_repo.delete_user(1)
