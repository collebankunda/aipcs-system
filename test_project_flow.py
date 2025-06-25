
def test_project_creation(client):
    response = client.post("/api/projects", json={
        "name": "Kitumbu Bridge",
        "location": "Mubende",
        "client": "UNRA",
        "budget": 10000000,
        "start_date": "2025-01-01",
        "end_date": "2025-12-31"
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Kitumbu Bridge"
