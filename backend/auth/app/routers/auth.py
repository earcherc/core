from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session
from typing import Annotated, Optional
from datetime import timedelta
from pydantic import BaseModel
from ..services import *
from app import Config, get_session


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


router = APIRouter()


@router.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}


@router.post("/register", status_code=201)
async def register(user: User, session: Session = Depends(get_session)):
    # Call register_user() to create a new user
    user_id = await register_user(user, session)

    if not user_id:
        raise HTTPException(status_code=400, detail="Registration failed")

    return {"user_id": user_id}


@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session),
):
    user = get_user(form_data.username, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username",
        )
    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
        )
    if Config.ACCESS_TOKEN_EXPIRE_MINUTES is None:
        raise ValueError("Invalid configuration: missing ACCESS_TOKEN_EXPIRE_MINUTES")
    access_token_expires = timedelta(minutes=int(Config.ACCESS_TOKEN_EXPIRE_MINUTES))
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me", response_model=User)
async def read_user_me(
    current_user: User = Depends(get_current_user),
):
    return current_user
