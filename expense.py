
from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import date

class Expense(BaseModel):
    id: Optional[UUID]
    boq_id: UUID
    project_id: UUID
    amount: float
    date: date
    category: str
    notes: Optional[str]
