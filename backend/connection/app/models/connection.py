from typing import Optional, List
from sqlmodel import Field, Relationship, SQLModel
from datetime import datetime
from sqlalchemy import UniqueConstraint
from sqlalchemy import CheckConstraint
from shared_schemas.enums import Gender, ConnectionStatus


class Connection(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_profile1_id: int = Field(
        default=None, foreign_key="userprofile.id", index=True
    )
    user_profile2_id: int = Field(
        default=None, foreign_key="userprofile.id", index=True
    )
    status: ConnectionStatus  # e.g., Pending, Accepted, Blocked
    created_at: datetime

    # Relationships
    # https://github.com/tiangolo/sqlmodel/issues/10
    user_profile1: UserProfile = Relationship(
        back_populates="sent_connections",
        sa_relationship_kwargs={
            "primaryjoin": "Connection.user_profile1_id == UserProfile.id"
        },
    )
    user_profile2: UserProfile = Relationship(
        back_populates="received_connections",
        sa_relationship_kwargs={
            "primaryjoin": "Connection.user_profile2_id == UserProfile.id"
        },
    )
