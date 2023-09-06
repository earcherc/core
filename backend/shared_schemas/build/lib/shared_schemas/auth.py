from typing import Optional

# Ignore error, resolved when package is installed in services
from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str
    password: str
    disabled: bool


class UserCreate(User):
    disabled: None


class UserGet(User):
    password: None


class UserUpdate(User):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    disabled: Optional[bool] = None


class UserInDB(User):
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str
    user_id: int
    disabled: bool
