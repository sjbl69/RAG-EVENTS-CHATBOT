from fastapi.testclient import TestClient
from api.main import app
from unittest.mock import patch

client = TestClient(app)


# TEST /ask 

@patch("api.rag_service.RAGService.ask")
def test_ask(mock_ask):
    mock_ask.return_value = "Réponse simulée"

    response = client.post(
        "/ask",
        json={"question": "Quels événements ?"}
    )

    assert response.status_code == 200
    data = response.json()

    assert data["answer"] == "Réponse simulée"


# TEST /rebuild 

@patch("api.rag_service.RAGService.rebuild")
def test_rebuild(mock_rebuild):
    mock_rebuild.return_value = "OK"

    response = client.post("/rebuild")

    assert response.status_code == 200
    data = response.json()

    assert "message" in data