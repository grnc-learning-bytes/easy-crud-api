from fastapi.testclient import TestClient
import pytest

from src.backend.server import app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)
