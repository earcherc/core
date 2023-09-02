from typing import Optional, List
from sqlmodel import Field, Relationship, SQLModel
from datetime import datetime
from sqlalchemy import UniqueConstraint
from sqlalchemy import CheckConstraint
from .enums import ConnectionStatus, Gender


# UserProfile replaces the User table in your core service
class UserProfile(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(default=None, unique=True, index=True)
    first_name: Optional[str] = Field(default=None)
    last_name: Optional[str] = Field(default=None)
    date_of_birth: Optional[datetime] = Field(default=None)
    gender: Optional[Gender] = Field(default=None)
    interested_in_gender: Optional[Gender] = Field(default=None)
    latitude: Optional[float] = Field(
        default=None, ge=-90, le=90
    )  # Valid latitude range is -90 to 90
    longitude: Optional[float] = Field(
        default=None, ge=-180, le=180
    )  # Valid longitude range is -180 to 180

    # Relationships
    profile_photos: List["ProfilePhoto"] = Relationship(back_populates="user_profile")
    sent_connections: List["Connection"] = Relationship(
        back_populates="user_profile1",
        sa_relationship_kwargs={"foreign_keys": "[Connection.user_profile1_id]"},
    )
    # https://github.com/tiangolo/sqlmodel/issues/10
    received_connections: List["Connection"] = Relationship(
        back_populates="user_profile2",
        sa_relationship_kwargs={"foreign_keys": "[Connection.user_profile2_id]"},
    )
    user_details: "UserProfileDetails" = Relationship(back_populates="user_profile")

    # Constraints
    class Config:
        table_constraints = [
            CheckConstraint(
                "LENGTH(first_name) > 0", name="check_first_name_non_empty"
            ),
            CheckConstraint("LENGTH(last_name) > 0", name="check_last_name_non_empty"),
        ]


class ProfilePhoto(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_profile_id: int = Field(default=None, foreign_key="userprofile.id", index=True)
    url: str
    caption: Optional[str] = Field(default=None)
    is_main: bool
    uploaded_at: datetime

    # Relationships
    user_profile: UserProfile = Relationship(back_populates="profile_photos")

    # Constraints
    class Config:
        table_constraints = [
            UniqueConstraint(
                "user_profile_id", "is_main", name="unique_main_photo_per_user"
            )
        ]


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


class UserProfileDetails(SQLModel, table=True):
    user_profile_id: int = Field(
        default=None, foreign_key="userprofile.id", primary_key=True
    )
    bio: Optional[str] = Field(default=None)
    job_title: Optional[str] = Field(default=None)
    company: Optional[str] = Field(default=None)
    school: Optional[str] = Field(default=None)
    hobbies: Optional[str] = Field(default=None)
    favorite_music: Optional[str] = Field(default=None)
    favorite_movies: Optional[str] = Field(default=None)
    favorite_books: Optional[str] = Field(default=None)

    # Relationships
    user_profile: UserProfile = Relationship(back_populates="user_details")


# Update forward references
UserProfile.update_forward_refs()
ProfilePhoto.update_forward_refs()
Connection.update_forward_refs()
UserProfileDetails.update_forward_refs()
