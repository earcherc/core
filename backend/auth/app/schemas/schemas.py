from typing import Optional, Union

from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str
    password: Union[str, None] = None
    disabled: Union[bool, None] = None


class UserInDB(User):
    id: int
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
    user_id: Optional[int] = None
    disabled: Optional[bool] = None
