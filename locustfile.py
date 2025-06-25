
from locust import HttpUser, task, between

class AIPCSUser(HttpUser):
    wait_time = between(1, 5)

    @task(1)
    def view_dashboard(self):
        self.client.get("/api/projects/")

    @task(2)
    def create_project(self):
        self.client.post("/api/projects/", json={
            "name": "Test Load Project",
            "location": "Kampala",
            "client": "LocustBot",
            "budget": 5000000,
            "start_date": "2025-07-01",
            "end_date": "2025-12-31",
            "status": "active"
        })
