
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_boq():
    response = client.post("/api/projects/boqs/", json={
        "project_id": "11111111-1111-1111-1111-111111111111",
        "item_desc": "Excavation",
        "unit": "m3",
        "quantity": 100.0,
        "unit_cost": 5000.0
    })
    assert response.status_code == 200
    assert "boq" in response.json()

def test_get_boqs():
    response = client.get("/api/projects/boqs/11111111-1111-1111-1111-111111111111")
    assert response.status_code == 200
