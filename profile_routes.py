
from fastapi import APIRouter, Depends
from models.profile import UserProfile
from controllers import profile_controller
from auth.dependencies import get_current_user

router = APIRouter()

@router.post("/")
def update_user_profile(profile: UserProfile, user: str = Depends(get_current_user)):
    profile.email = user
    return profile_controller.update_profile(profile)

@router.get("/")
def fetch_user_profile(user: str = Depends(get_current_user)):
    return profile_controller.get_profile(user)
