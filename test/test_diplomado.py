import pytest
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_get_diplomado():
    response = client.get("/diplomado")
    assert response.status_code == 200
    assert response.json() == "Welcome diplomado"
