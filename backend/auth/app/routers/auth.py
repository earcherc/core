from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services import user_service

router = APIRouter()


class UserRegistration(BaseModel):
    username: str
    email: str
    password: str


@router.post("/register", status_code=201)
async def register_user(user: UserRegistration):
    # Call user_service.register_user() to create a new user
    user_id = await user_service.register_user(user)

    if not user_id:
        raise HTTPException(status_code=400, detail="Registration failed")

    return {"user_id": user_id}
