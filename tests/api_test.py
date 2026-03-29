from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_ask():
    response = client.post(
        "/ask",
        json={"question": "Quels événements à Lyon ce week-end ?"}
    )

    assert response.status_code == 200
    data = response.json()

    assert "answer" in data
    assert isinstance(data["answer"], str)


def test_rebuild():
    response = client.post("/rebuild")

    assert response.status_code == 200
    data = response.json()

    assert "message" in data