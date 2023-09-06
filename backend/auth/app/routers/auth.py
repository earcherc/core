from fastapi import APIRouter, HTTPException, Depends, Response, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session
from datetime import timedelta
from shared_schemas.auth import UserCreate, Token
from ..services import (
    get_user_func,
    verify_password_func,
    create_access_token_func,
    register_user_func,
)
from ..models import User as UserTable
from ..message_handlers import publish_to_queue
from app import Config, get_session
from pydantic import BaseModel


router = APIRouter()


class UserId(BaseModel):
    user_id: int


@router.post("/register", response_model=UserId, status_code=201)
async def register(user: UserCreate, session: Session = Depends(get_session)):
    user_id = await register_user_func(user, session)

    if not user_id:
        raise HTTPException(status_code=400, detail="Registration failed")

    # Create a dictionary to send as a message
    # Publish the dictionary to the queue
    message_dict = {"user_id": user_id, "action": "register"}
    publish_to_queue(message_dict)

    return {"user_id": user_id}


@router.post("/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session),
):
    if Config.ACCESS_TOKEN_EXPIRE_MINUTES is None:
        raise ValueError("Invalid configuration: missing ACCESS_TOKEN_EXPIRE_MINUTES")

    user = await get_user_func(form_data.username, session)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username",
        )

    if not await verify_password_func(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
        )

    access_token_expires = timedelta(minutes=int(Config.ACCESS_TOKEN_EXPIRE_MINUTES))
    access_token = await create_access_token_func(
        data={"sub": user.username, "user_id": user.id, "disabled": user.disabled},
        expires_delta=access_token_expires,
    )

    if not access_token:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not create access token",
        )

    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/logout")
async def logout(response: Response):
    response.delete_cookie(key="access_token")
    return {"detail": "Successfully logged out"}


class UserInfo(BaseModel):
    username: str
    email: str
    disabled: bool


@router.get("/user-info/{user_id}", response_model=UserInfo)
async def get_user_info(user_id: int, session: Session = Depends(get_session)):
    user = UserTable.get_or_none(session, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user
