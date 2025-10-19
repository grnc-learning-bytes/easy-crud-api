from fastapi.testclient import TestClient


def test_can_delete_task(client: TestClient):
    res = client.post(
        "/tasks",
        json={
            "name": "Validate deletions",
            "description": "Implement tests for delete events.",
            "priority": "critical",
            "status": "ready",
            "tags": ["events"],
        },
    )
    id: int = res.json()["data"]["id"]
    res = client.delete(f"/tasks/{id}")
    assert res.status_code == 200


def test_cant_delete_missing_task(client: TestClient):
    id: int = -1
    res = client.delete(f"/tasks/{id}")
    assert res.status_code == 404
