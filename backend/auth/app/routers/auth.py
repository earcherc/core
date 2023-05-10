from fastapi import APIRouter, HTTPException, Depends, status
from app.services import user_service
from sqlmodel import Session
from app.database import get_session

router = APIRouter()


@router.post("/register", status_code=201)
async def register_user(
    user: user_service.User, session: Session = Depends(get_session)
):
    # Call user_service.register_user() to create a new user
    user_id = await user_service.register_user(user, session)

    if not user_id:
        raise HTTPException(status_code=400, detail="Registration failed")

    return {"user_id": user_id}


@router.post("/login")
async def login(username: str, password: str, session: Session = Depends(get_session)):
    user = user_service.get_user(username, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username",
        )
    if not user_service.verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
        )
    return {"username": username}


@router.get("/users/me", response_model=user_service.User)
async def read_user_me(username: str, session: Session = Depends(get_session)):
    user = user_service.get_user(username, session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return user
