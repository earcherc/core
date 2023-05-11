from sqlmodel import SQLModel, Field, Session
from typing import Optional

metadata = SQLModel.metadata


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(default=None, index=True, unique=True)
    email: str = Field(default=None, index=True, unique=True)
    password: str

    @classmethod
    def get_or_none(cls, session: Session, id_: int) -> Optional["User"]:
        return session.get(cls, id_)
