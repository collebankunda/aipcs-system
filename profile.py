
from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class UserProfile(BaseModel):
    id: Optional[UUID]
    email: str
    full_name: Optional[str]
    phone: Optional[str]
    company_role: Optional[str]
