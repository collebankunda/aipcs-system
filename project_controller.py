
from models.project import Project
import uuid

# Simulated in-memory DB
projects_db = []

def create_project(project: Project):
    project.id = str(uuid.uuid4())
    projects_db.append(project.dict())
    return {"message": "Project created", "project": project}

def list_projects():
    return projects_db
