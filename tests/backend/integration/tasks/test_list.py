from fastapi.testclient import TestClient

from src.backend.models.responses.tasks import ListTasksResponse


def test_can_list_tasks(client: TestClient):
    res = client.get("/tasks?page=1")
    assert res.status_code == 200
    ListTasksResponse.model_validate(res.json())


def test_list_tasks_without_page_fails(client: TestClient):
    res = client.get("/tasks")
    assert res.status_code == 422


def test_list_tasks_all_have_filter_tags(client: TestClient):
    client.post(
        "/tasks",
        json={
            "name": "Create tests",
            "description": "Some tests.",
            "priority": "low",
            "status": "backlog",
            "tags": ["chore"],
        },
    )
    client.post(
        "/tasks",
        json={
            "name": "Create tests 2",
            "description": "More tests",
            "priority": "minor",
            "status": "backlog",
            "tags": ["more-chore"],
        },
    )
    res = client.get("/tasks?page=1&tags[]=chore")
    assert res.status_code == 200
    body = res.json()
    ListTasksResponse.model_validate(body)
    task_tags: list[list[str]] = [d["attributes"]["tags"] for d in body["data"]]
    assert all(["chore" in t for t in task_tags])
