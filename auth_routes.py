
from fastapi import APIRouter, HTTPException
from models.user import User
from auth.auth_handler import hash_password, verify_password, create_token

router = APIRouter()
fake_users_db = {}

@router.post("/register")
def register(user: User):
    if user.email in fake_users_db:
        raise HTTPException(status_code=400, detail="Email already registered")
    user.password = hash_password(user.password)
    fake_users_db[user.email] = user.dict()
    return {"message": "User registered successfully"}

@router.post("/login")
def login(user: User):
    db_user = fake_users_db.get(user.email)
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
