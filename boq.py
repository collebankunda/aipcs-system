
from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class BOQItem(BaseModel):
    id: Optional[UUID]
    project_id: UUID
    item_desc: str
    unit: str
    quantity: float
    unit_cost: float
