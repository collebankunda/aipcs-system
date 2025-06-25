
from models.profile import UserProfile
from uuid import uuid4

profile_db = {}

def update_profile(profile: UserProfile):
    profile.id = uuid4()
    profile_db[profile.email] = profile.dict()
    return {"message": "Profile updated", "profile": profile}

def get_profile(email: str):
    return profile_db.get(email, {})
