
from fastapi import APIRouter, Depends
from controllers import project_controller
from models.project import Project

router = APIRouter()

@router.post("/")
from auth.dependencies import get_current_user

def create_project(project: Project, user: str = Depends(get_current_user)):
    return project_controller.create_project(project)

@router.get("/")
def list_projects():
    return project_controller.list_projects()
