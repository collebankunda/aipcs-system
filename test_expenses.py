
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_expense():
    response = client.post("/api/projects/expenses/", json={
        "boq_id": "22222222-2222-2222-2222-222222222222",
        "project_id": "11111111-1111-1111-1111-111111111111",
        "amount": 250000,
        "date": "2025-01-20",
        "category": "materials",
        "notes": "Purchased cement"
    })
    assert response.status_code == 200
    assert "expense" in response.json()

def test_get_expenses():
    response = client.get("/api/projects/expenses/11111111-1111-1111-1111-111111111111")
    assert response.status_code == 200
