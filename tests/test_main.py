from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_saludar():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensaje": "¡Hola, mundo!"}

def test_saludar_persona():
    response = client.get("/saludar/Juan")
    assert response.status_code == 200
    assert response.json() == {"mensaje": "¡Hola, Juan!"}