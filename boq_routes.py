
from fastapi import APIRouter
from models.boq import BOQItem
from controllers import boq_controller

router = APIRouter()

@router.post("/")
def create_boq(boq: BOQItem):
    return boq_controller.create_boq(boq)

@router.get("/{project_id}")
def get_boqs(project_id: str):
    return boq_controller.list_boqs(project_id)
