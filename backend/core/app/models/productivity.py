from typing import Optional, List
from sqlmodel import Field, Relationship, SQLModel, Session
from datetime import datetime

metadata = SQLModel.metadata


class UserProfile(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(default=None, unique=True)  # user_id from the auth service

    # Additional user profile fields
    favorite_color: Optional[str] = Field(default=None)
    bio: Optional[str] = Field(default=None)

    # Relationships
    study_blocks: List["StudyBlock"] = Relationship(back_populates="user_profile")
    daily_goals: List["DailyGoal"] = Relationship(back_populates="user_profile")
    study_categories: List["StudyCategory"] = Relationship(
        back_populates="user_profile"
    )


class StudyBlock(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    start: datetime
    end: datetime
    title: str
    rating: float = Field(gt=0, lt=5)  # ratings should be between 0 and 5

    # Foreign keys
    user_profile_id: int = Field(foreign_key="userprofile.id")
    daily_goal_id: int = Field(foreign_key="dailygoal.id")
    study_category_id: int = Field(foreign_key="studycategory.id")

    # Relationships
    user_profile: UserProfile = Relationship(back_populates="study_blocks")
    daily_goal: "DailyGoal" = Relationship(back_populates="study_blocks")
    study_category: "StudyCategory" = Relationship(back_populates="study_blocks")


class DailyGoal(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    quantity: int
    block_size: int

    # Foreign keys
    user_profile_id: int = Field(foreign_key="userprofile.id", index=True)

    # Relationships
    user_profile: UserProfile = Relationship(back_populates="daily_goals")
    study_blocks: List["StudyBlock"] = Relationship(back_populates="daily_goal")


class StudyCategory(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str

    # Relationships
    study_blocks: List["StudyBlock"] = Relationship(back_populates="study_category")
    user_profiles: List[UserProfile] = Relationship(back_populates="study_categories")


class UserProfileCategoryLink(SQLModel, table=True):
    user_profile_id: Optional[int] = Field(
        default=None, foreign_key="userprofile.id", primary_key=True
    )
    study_category_id: Optional[int] = Field(
        default=None, foreign_key="studycategory.id", primary_key=True
    )

    # Relationships
    user_profile: "UserProfile" = Relationship(back_populates="category_links")
    study_category: "StudyCategory" = Relationship(back_populates="user_profile_links")


UserProfile.update_forward_refs()
StudyBlock.update_forward_refs()
DailyGoal.update_forward_refs()
StudyCategory.update_forward_refs()
UserProfileCategoryLink.update_forward_refs()
