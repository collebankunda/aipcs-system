
from models.boq import BOQItem
import uuid

boq_db = []

def create_boq(boq: BOQItem):
    boq.id = uuid.uuid4()
    boq_db.append(boq.dict())
    return {"message": "BOQ item created", "boq": boq}

def list_boqs(project_id):
    return [item for item in boq_db if item["project_id"] == project_id]
