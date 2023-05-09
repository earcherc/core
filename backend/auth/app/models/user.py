from typing import Optional
from sqlmodel import SQLModel, Field, Session


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    email: str = Field(unique=True, index=True)
    password: str

    @classmethod
    def get_or_none(cls, session: Session, id_: int) -> Optional['User']:
        return session.get(cls, id_)