from fastapi import APIRouter, HTTPException, Depends, Response, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session
from datetime import timedelta
from ..schemas import User, Token
from ..services import *
from app import Config, get_session


router = APIRouter()


@router.post("/register", status_code=201)
async def register(user: User, session: Session = Depends(get_session)):
    # Call register_user() to create a new user
    user_id = await register_user(user, session)

    if not user_id:
        raise HTTPException(status_code=400, detail="Registration failed")

    return {"user_id": user_id}


@router.post("/login", response_model=Token)
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


@router.post("/logout")
async def logout(response: Response):
    response.delete_cookie(key="access_token")
    return {"detail": "Successfully logged out"}
