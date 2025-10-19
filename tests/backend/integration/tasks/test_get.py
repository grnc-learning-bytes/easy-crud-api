from fastapi.testclient import TestClient

from src.backend.models.responses.tasks import GetTaskResponse


def test_can_get_task(client: TestClient):
    res = client.post(
        "/tasks",
        json={
            "name": "Create tests 2",
            "description": "More tests",
            "priority": "minor",
            "status": "backlog",
            "tags": ["more-chore"],
        },
    )
    id: int = res.json()["data"]["id"]
    res = client.get(f"/tasks/{id}")
    assert res.status_code == 200
    GetTaskResponse.model_validate(res.json())


def test_cant_get_missing_task(client: TestClient):
    res = client.get("/tasks/-1")
    assert res.status_code == 404
