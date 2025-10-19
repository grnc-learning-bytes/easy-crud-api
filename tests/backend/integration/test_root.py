from fastapi.testclient import TestClient


def test_health_check_works(client: TestClient):
    res = client.get("/health")
    res.raise_for_status()
    assert res.status_code == 200  # Success


def test_docs_redirect(client: TestClient):
    res = client.get("/", follow_redirects=False)
    assert res.status_code == 307  # Temporary Redirect
    assert res.headers.get("location", None) == "/docs"


def test_docs_redirect_works(client: TestClient):
    res = client.get("/")
    assert res.status_code == 200
