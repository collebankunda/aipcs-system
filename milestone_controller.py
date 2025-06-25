
from models.milestone import Milestone
import uuid

milestone_db = []

def create_milestone(milestone: Milestone):
    milestone.id = uuid.uuid4()
    milestone_db.append(milestone.dict())
    return {"message": "Milestone created", "milestone": milestone}

def list_milestones(project_id):
    return [m for m in milestone_db if m["project_id"] == project_id]
