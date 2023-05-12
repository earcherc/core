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
    user_profile_id: int
    daily_goal_id: int
    study_category_id: int


class StudyBlockUpdate(StudyBlock):
    pass


class StudyBlockInDB(StudyBlock):
    id: int

    class Config:
        orm_mode = True


class DailyGoal(BaseModel):
    quantity: int
    block_size: int


class DailyGoalCreate(DailyGoal):
    user_profile_id: int


class DailyGoalUpdate(DailyGoal):
    pass


class DailyGoalInDB(DailyGoal):
    id: int

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
    user_profile_id: int
    study_category_id: int


class UserProfileCategoryLinkUpdate(UserProfileCategoryLink):
    pass


class UserProfileCategoryLinkInDB(UserProfileCategoryLink):
    user_profile_id: int
    study_category_id: int

    class Config:
        orm_mode = True
