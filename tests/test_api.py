from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_validation_rejects_empty_document_type():
    response = client.post(
        "/generate",
        json={
            "document_type": "",
            "parties": "A and B",
            "terms": "Payment within 30 days",
            "effective_date": "April 15, 2026",
        },
    )
    assert response.status_code == 422
