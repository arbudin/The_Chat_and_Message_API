import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_post_chat():
    response = client.post("/chats/", json={"title": "Тестовый чат"})
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["title"] == "Тестовый чат"
