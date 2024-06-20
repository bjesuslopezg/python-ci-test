import pytest
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_get_sabana():
    response = client.get("/sabana")
    assert response.status_code == 200
    assert response.json() == "Welcome"
