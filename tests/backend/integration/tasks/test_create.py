from fastapi.testclient import TestClient
from httpx import HTTPStatusError
import pytest

from src.backend.models.responses.tasks import CreateTaskResponse


def test_can_create_task(client: TestClient):
    res = client.post("/tasks", data={
        "name": "Create tests",
        "description": "Create behavioral tests for testing the api end to end.",
        "priority": "high",
        "status": "backlog",
    })
    res.raise_for_status()
    assert res.status_code == 201
    CreateTaskResponse.model_validate(res.json())


def test_can_create_tasks_with_same_content(client: TestClient):
    task_content = {
        "name": "Create tests",
        "description": "Create behavioral tests for testing the api end to end.",
        "priority": "high",
        "status": "backlog",
    }

    res = client.post("/tasks", data=task_content)
    res.raise_for_status()
    assert res.status_code == 201
    CreateTaskResponse.model_validate(res.json())

    res = client.post("/tasks", data=task_content)
    res.raise_for_status()
    assert res.status_code == 201
    CreateTaskResponse.model_validate(res.json())


def test_cant_create_tasks_with_invalid_schema(client: TestClient):
    res = client.post("/tasks", data={"invalid": "schema"})
    assert res.status_code == 400


def test_cant_create_tasks_with_incomplete_schema(client: TestClient):
    res = client.post("/tasks", data={"name": "My Task"})
    assert res.status_code == 400
