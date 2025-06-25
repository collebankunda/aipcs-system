
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_milestone():
    response = client.post("/api/projects/milestones/", json={
        "project_id": "11111111-1111-1111-1111-111111111111",
        "title": "Site Clearance",
        "due_date": "2025-02-15",
        "actual_date": "2025-02-16",
        "status": "done"
    })
    assert response.status_code == 200
    assert "milestone" in response.json()

def test_get_milestones():
    response = client.get("/api/projects/milestones/11111111-1111-1111-1111-111111111111")
    assert response.status_code == 200
