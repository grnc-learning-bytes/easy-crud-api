from dependency_injector import providers
import pytest
import os
from typing import Generator

from src.backend.settings.container import Container
from src.backend.repositories.users.in_memory import InMemoryUserRepository


@pytest.fixture
def faker_container() -> Generator[Container]:
    # Setup fake environment variables
    os.environ["DATABASE_DSN"] = "postgres://user:pass@localhost:5432/foobar"

    # Create container with fakers
    container = Container()
    container.build()
    with container.override_providers(
        user_repo=providers.Singleton(InMemoryUserRepository)
    ):
        yield container
