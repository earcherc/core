from enum import Enum
from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List
from ..models import ConnectionStatus, Gender


class UserProfile(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    date_of_birth: Optional[datetime] = None
    gender: Optional[Gender] = None
    interested_in_gender: Optional[Gender] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None


class UserProfileCreate(UserProfile):
    user_id: int


class UserProfileUpdate(UserProfile):
    pass


class UserProfileInDB(UserProfile):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class Connection(BaseModel):
    user_profile1_id: int
    user_profile2_id: int
    status: ConnectionStatus
    created_at: datetime


class ConnectionCreate(Connection):
    pass


class ConnectionUpdate(Connection):
    pass


class ConnectionInDB(Connection):
    id: int

    class Config:
        orm_mode = True


class ProfilePhoto(BaseModel):
    user_profile_id: int
    url: str
    caption: Optional[str] = None
    is_main: bool
    uploaded_at: datetime


class UserProfileDetails(BaseModel):
    user_profile_id: int
    bio: Optional[str] = None
    job_title: Optional[str] = None
    company: Optional[str] = None
    school: Optional[str] = None
    hobbies: Optional[str] = None
    favorite_music: Optional[str] = None
    favorite_movies: Optional[str] = None
    favorite_books: Optional[str] = None
