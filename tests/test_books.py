from fastapi.testclient import TestClient
from app.main import app
from app.cache import redis_client

client = TestClient(app)

def test_create_book():
    response = client.post("/books/", json={"title": "Test Book", "author": "Tester"})
    assert response.status_code == 201
    assert response.json()["title"] == "Test Book"


def test_get_books():
    response = client.get("/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_cache_miss_fallback(monkeypatch):
    # Simulate Redis Down
    monkeypatch.setattr("app.cache.redis_client", None)

    response = client.get("/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)