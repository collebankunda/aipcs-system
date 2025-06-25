
from fastapi import APIRouter, Depends
from auth.dependencies import require_role
from controllers import activity_log_controller

router = APIRouter()

@router.get("/")
def view_logs(user: str = Depends(require_role("admin"))):
    return activity_log_controller.get_logs()
