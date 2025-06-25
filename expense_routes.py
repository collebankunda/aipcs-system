
from fastapi import APIRouter
from models.expense import Expense
from controllers import expense_controller

router = APIRouter()

@router.post("/")
def create_expense(expense: Expense):
    return expense_controller.create_expense(expense)

@router.get("/{project_id}")
def get_expenses(project_id: str):
    return expense_controller.list_expenses(project_id)
