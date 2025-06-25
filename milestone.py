
from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import date

class Milestone(BaseModel):
    id: Optional[UUID]
    project_id: UUID
    title: str
    due_date: date
    actual_date: Optional[date]
    status: str
