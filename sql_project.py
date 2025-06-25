
from sqlalchemy import Column, String, Float, Date
from uuid import uuid4
from server.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    name = Column(String, index=True)
    location = Column(String)
    client = Column(String)
    budget = Column(Float)
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String)
