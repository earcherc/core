from datetime import datetime, timedelta
from fastapi import HTTPException, Depends

from ..models import User as UserTable
from passlib.context import CryptContext
from sqlmodel import Session, col, or_, select
from jose import jwt
from typing import Optional, Dict
from app import Config
from shared_schemas.auth import UserInDB, UserCreate


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_user_func(username: str, session: Session) -> Optional[UserInDB]:
    user_statement = select(UserTable).where(UserTable.username == username)
    user = session.exec(user_statement).first()
    if user is None:
        return None

    return UserInDB.from_orm(user)


async def register_user_func(user_data: UserCreate, session: Session) -> int:
    user_exists_statement = select(UserTable).where(
        or_(
            col(UserTable.username) == user_data.username,
            col(UserTable.email) == user_data.email,
        )
    )
    existing_user = session.exec(user_exists_statement).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Username or email already exists")

    hashed_password = pwd_context.hash(user_data.password)
    new_user = UserTable(
        username=user_data.username, email=user_data.email, password=hashed_password
    )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user.id


async def verify_password_func(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


async def create_access_token_func(
    data: Dict, expires_delta: Optional[timedelta] = None
) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})

    if Config.SECRET_KEY is None or Config.ALGORITHM is None:
        raise ValueError("Invalid configuration: missing SECRET_KEY or ALGORITHM")

    return jwt.encode(to_encode, Config.SECRET_KEY, algorithm=Config.ALGORITHM)
