from fastapi.testclient import TestClient


def test_can_list(client: TestClient):
    res = client.get("/tasks?page=1")
    res.raise_for_status()
    assert res.status_code == 200


def test_list_without_page_fails(client: TestClient):
    res = client.get("/tasks")
    assert res.status_code == 422
