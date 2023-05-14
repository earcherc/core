from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel


class UserProfile(BaseModel):
    favorite_color: Optional[str] = None
    bio: Optional[str] = None


class UserProfileCreate(UserProfile):
    user_id: int


class UserProfileUpdate(UserProfile):
    pass


class UserProfileInDB(UserProfile):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class StudyBlock(BaseModel):
    start: datetime
    end: datetime
    title: str
    rating: float


class StudyBlockCreate(StudyBlock):
    user_id: int
    daily_goal_id: int
    study_category_id: int


class StudyBlockUpdate(BaseModel):
    start: Optional[datetime] = None
    end: Optional[datetime] = None
    title: Optional[str] = None
    rating: Optional[float] = None
    daily_goal_id: Optional[int] = None
    study_category_id: Optional[int] = None


class StudyBlockInDB(StudyBlock):
    id: int
    user_id: int  # added user_id

    class Config:
        orm_mode = True


class DailyGoal(BaseModel):
    quantity: int
    block_size: int


class DailyGoalCreate(DailyGoal):
    user_id: int


class DailyGoalUpdate(DailyGoal):
    pass


class DailyGoalInDB(DailyGoal):
    id: int
    user_id: int  # added user_id

    class Config:
        orm_mode = True


class StudyCategory(BaseModel):
    title: str


class StudyCategoryCreate(StudyCategory):
    pass


class StudyCategoryUpdate(StudyCategory):
    pass


class StudyCategoryInDB(StudyCategory):
    id: int

    class Config:
        orm_mode = True


class UserProfileCategoryLink(BaseModel):
    pass


class UserProfileCategoryLinkCreate(UserProfileCategoryLink):
    user_id: int
    study_category_id: int


class UserProfileCategoryLinkUpdate(UserProfileCategoryLink):
    pass


class UserProfileCategoryLinkInDB(UserProfileCategoryLink):
    user_id: int
    study_category_id: int

    class Config:
        orm_mode = True
