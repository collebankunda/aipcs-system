
from pydantic import BaseModel
from typing import Optional
from datetime import date

class Project(BaseModel):
    id: Optional[str]
    name: str
    location: str
    client: str
    budget: float
    start_date: date
    end_date: date
    status: str
