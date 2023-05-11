from datetime import datetime, timedelta
from fastapi import HTTPException, Depends, status
from app.models import User as UserTable
from pydantic import BaseModel
from passlib.context import CryptContext
from sqlmodel import Session, col, or_, select
from jose import JWTError, jwt
from typing import Annotated, Optional, Union
from app.database import get_session
from fastapi.security import OAuth2PasswordBearer
from config import Config

from app.routers.auth import TokenData


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class User(BaseModel):
    username: str
    email: str
    password: Union[str, None] = None
    disabled: Union[bool, None] = None


class UserInDB(User):
    hashed_password: str


def get_user(
    username: str, session: Session = Depends(get_session)
) -> Optional[UserInDB]:
    statement = select(UserTable).where(UserTable.username == username)
    user = session.exec(statement).first()
    if user:
        return UserInDB(
            username=user.username, email=user.email, hashed_password=user.password
        )


async def register_user(user_data: User, session: Session):
    # Check if the username or email already exists in the database
    statement = select(UserTable).where(
        or_(
            # Use col to trick editor that this is a speical
            # SQLModel column and not just a optional class instance attribute
            col(UserTable.username) == user_data.username,
            col(UserTable.email) == user_data.email,
        )
    )
    # Use the newer session.exec over session.query; resembles actual SQL more
    # Also, session.get just returns the id of the db object
    existing_user = session.exec(statement).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username or email already exists")

    # Hash the user's password
    hashed_password = get_password_hash(user_data.password)

    # Create a new user with the hashed password
    new_user = UserTable(
        username=user_data.username, email=user_data.email, password=hashed_password
    )

    # Add the new user to the session
    session.add(new_user)

    # Commit the transaction
    session.commit()

    # Refresh the user object to get the ID assigned by the database
    session.refresh(new_user)

    return new_user.id


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    if Config.SECRET_KEY is None or Config.ALGORITHM is None:
        raise ValueError("Invalid configuration: missing SECRET_KEY or ALGORITHM")
    encoded_jwt = jwt.encode(to_encode, Config.SECRET_KEY, algorithm=Config.ALGORITHM)
    return encoded_jwt


async def get_current_user(
    token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        if Config.SECRET_KEY is None or Config.ALGORITHM is None:
            raise ValueError("Invalid configuration: missing SECRET_KEY or ALGORITHM")
        payload = jwt.decode(token, Config.SECRET_KEY, algorithms=[Config.ALGORITHM])
        username: str = payload.get("sub", "")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except (JWTError, ValueError) as e:
        raise credentials_exception from e
    user = get_user(username, session)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
