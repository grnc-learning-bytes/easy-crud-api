from fastapi.testclient import TestClient


def test_can_update_task(client: TestClient):
    res = client.post(
        "/tasks",
        json={
            "name": "Create tests",
            "description": "Create behavioral tests for testing the api end to end.",
            "priority": "high",
            "status": "backlog",
            "tags": ["chore"],
        },
    )
    id: int = res.json()["data"]["id"]
    res = client.put(
        f"/tasks/{id}",
        json={
            "name": "Damn all the tests",
            "description": "All my tests are failingggg.",
            "priority": "critical",
            "status": "in_progress",
            "tags": ["pain"],
        },
    )
    assert res.status_code == 204


def test_cant_update_missing_task(client: TestClient):
    res = client.put(
        "/tasks/-1",
        json={
            "name": "Damn all the tests",
            "description": "All my tests are failingggg.",
            "priority": "critical",
            "status": "in_progress",
            "tags": ["pain"],
        },
    )
    assert res.status_code == 404
