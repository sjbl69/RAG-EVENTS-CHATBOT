import requests

BASE_URL = "http://127.0.0.1:8000"


def test_ask():
    response = requests.post(
        f"{BASE_URL}/ask",
        json={"question": "Quels événements à Lyon ce week-end ?"}
    )

    assert response.status_code == 200
    data = response.json()

    assert "answer" in data


def test_rebuild():
    response = requests.post(f"{BASE_URL}/rebuild")

    assert response.status_code == 200