from sqlmodel import SQLModel, Field, Session
from typing import Optional


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(max_length=100, unique=True)
    email: str = Field(max_length=100, unique=True)
    password: str = Field(max_length=100)

    @classmethod
    def get_or_none(cls, session: Session, id_: int) -> Optional["User"]:
        return session.get(cls, id_)
