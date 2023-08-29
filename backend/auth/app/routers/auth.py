from fastapi import APIRouter, HTTPException, Depends, Response, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session
from datetime import timedelta
from ..schemas import User, Token
from ..services import (
    get_user,
    verify_password,
    create_access_token,
    register_user,
)
from ..message_handlers import publish_to_queue
from app import Config, get_session


router = APIRouter()


@router.post("/register", status_code=201)
async def register(user: User, session: Session = Depends(get_session)):
    # Call register_user() to create a new user
    user_id = await register_user(user, session)

    if not user_id:
        raise HTTPException(status_code=400, detail="Registration failed")

    publish_to_queue(f"New user registered with ID {user_id}")

    return {"user_id": user_id}


@router.post("/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session),
):
    if Config.ACCESS_TOKEN_EXPIRE_MINUTES is None:
        raise ValueError("Invalid configuration: missing ACCESS_TOKEN_EXPIRE_MINUTES")

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

    access_token_expires = timedelta(minutes=int(Config.ACCESS_TOKEN_EXPIRE_MINUTES))
    access_token = create_access_token(
        data={"sub": user.username, "user_id": user.id, "disabled": user.disabled},
        expires_delta=access_token_expires,
    )

    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/logout")
async def logout(response: Response):
    response.delete_cookie(key="access_token")
    return {"detail": "Successfully logged out"}
