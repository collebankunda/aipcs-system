
from fastapi import APIRouter
from models.milestone import Milestone
from controllers import milestone_controller

router = APIRouter()

@router.post("/")
def create_milestone(milestone: Milestone):
    return milestone_controller.create_milestone(milestone)

@router.get("/{project_id}")
def get_milestones(project_id: str):
    return milestone_controller.list_milestones(project_id)
