from fastapi.testclient import TestClient
from src.github_api_server import app
from src.github_api_server import Gist
from typing import List

client = TestClient(app)


def test_get_user_gists():
    response = client.get("/octocat")
    assert response.status_code == 200
    data = response.json()

    assert all(map(lambda x: Gist.model_validate(x), data))
    # Test max pagination limit
    assert len(data) <= 10


def test_user_not_found():
    response = client.get("/non-existent-user-1234")
    assert response.status_code == 404


def test_pagination():
    response = client.get("/octocat", params={"page_num": 1, "results_per_page": 3})
    assert response.status_code == 200
    data = response.json()
    assert all(map(lambda x: Gist.model_validate(x), data))
    assert len(data) <= 3
