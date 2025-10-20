from dependency_injector.providers import Singleton
from fastapi.testclient import TestClient
import pytest
from typing import Generator

from src.backend.repositories.tasks.in_memory import InMemoryTaskRepo
from src.backend.settings.container import Container
from src.backend.server import app


@pytest.fixture
def client() -> Generator[TestClient]:
    container = Container.container()
    with container.override_providers(task_repo=Singleton(InMemoryTaskRepo)):
        yield TestClient(app)
