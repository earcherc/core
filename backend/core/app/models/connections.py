from typing import Optional, List
from sqlmodel import Field, Relationship, SQLModel
from datetime import datetime
from sqlalchemy import UniqueConstraint
from sqlalchemy import CheckConstraint
from shared_schemas.enums import Gender, ConnectionStatus


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
UserProfileDetails.update_forward_refs()
