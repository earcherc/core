from typing import Optional, Union

from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str
    password: Union[str, None] = None
    disabled: Union[bool, None] = None


class UserInDB(User):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
