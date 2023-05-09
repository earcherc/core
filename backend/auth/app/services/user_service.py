from app.models import User
from fastapi import HTTPException
from sqlmodel import Session
from typing import Optional
import bcrypt

from app.routers.auth import UserRegistration



async def register_user(user_data: UserRegistration):
    # Check if the username or email already exists in the database
    existing_user = await User.get_or_none(
        username=user_data.username
    ) or await User.get_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username or email already exists")

    # Hash the user's password
    hashed_password = bcrypt.hash(user_data.password)

    # Create a new user with the hashed password
    new_user = User(
        username=user_data.username, email=user_data.email, password=hashed_password
    )

    # Save the new user to the database
    await new_user.save()

    return new_user.id

def get_user_by_id(session: Session, user_id: int) -> Optional[User]:
    return User.get_or_none(session, user_id)
