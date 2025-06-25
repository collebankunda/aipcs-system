
from models.expense import Expense
import uuid

expense_db = []

def create_expense(expense: Expense):
    expense.id = uuid.uuid4()
    expense_db.append(expense.dict())
    return {"message": "Expense recorded", "expense": expense}

def list_expenses(project_id):
    return [exp for exp in expense_db if exp["project_id"] == project_id]
