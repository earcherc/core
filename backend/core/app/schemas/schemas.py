from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel


class UserProfileBase(BaseModel):
    favorite_color: Optional[str] = None
    bio: Optional[str] = None


class UserProfileCreate(UserProfileBase):
    user_id: int


class UserProfileUpdate(UserProfileBase):
    pass


class UserProfileInDB(UserProfileBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class StudyBlockBase(BaseModel):
    start: datetime
    end: datetime
    title: str
    rating: float


class StudyBlockCreate(StudyBlockBase):
    user_profile_id: int
    daily_goal_id: int
    study_category_id: int


class StudyBlockUpdate(StudyBlockBase):
    pass


class StudyBlockInDB(StudyBlockBase):
    id: int

    class Config:
        orm_mode = True


class DailyGoalBase(BaseModel):
    quantity: int
    block_size: int


class DailyGoalCreate(DailyGoalBase):
    user_profile_id: int


class DailyGoalUpdate(DailyGoalBase):
    pass


class DailyGoalInDB(DailyGoalBase):
    id: int

    class Config:
        orm_mode = True


class StudyCategoryBase(BaseModel):
    title: str


class StudyCategoryCreate(StudyCategoryBase):
    pass


class StudyCategoryUpdate(StudyCategoryBase):
    pass


class StudyCategoryInDB(StudyCategoryBase):
    id: int

    class Config:
        orm_mode = True


class UserProfileCategoryLinkBase(BaseModel):
    pass


class UserProfileCategoryLinkCreate(UserProfileCategoryLinkBase):
    user_profile_id: int
    study_category_id: int


class UserProfileCategoryLinkUpdate(UserProfileCategoryLinkBase):
    pass


class UserProfileCategoryLinkInDB(UserProfileCategoryLinkBase):
    user_profile_id: int
    study_category_id: int

    class Config:
        orm_mode = True
