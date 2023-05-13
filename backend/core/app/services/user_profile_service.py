from typing import Optional
from ..models import UserProfile as UserProfileTable
from ..schemas import UserProfileInDB, UserProfile, UserProfileCreate
from sqlmodel import Session, select
from fastapi import HTTPException


async def get_user_profile_func(
    user_id: int, session: Session
) -> Optional[UserProfileInDB]:
    user_profile_statement = select(UserProfileTable).where(
        UserProfileTable.user_id == user_id
    )
    user_profile = session.exec(user_profile_statement).first()
    if not user_profile:
        raise HTTPException(
            status_code=400, detail="User profile with this user_id already exists"
        )

    return UserProfileInDB(**user_profile.__dict__)


async def create_user_profile_func(
    user_profile_data: UserProfileCreate, session: Session
):
    existing_user_profile = session.exec(
        select(UserProfileTable).where(
            UserProfileTable.user_id == user_profile_data.user_id
        )
    ).first()

    if existing_user_profile is not None:
        raise HTTPException(
            status_code=400, detail="User profile with this user_id already exists"
        )

    user_profile = UserProfileTable(**user_profile_data.dict())

    session.add(user_profile)
    session.commit()
    session.refresh(user_profile)

    return UserProfileInDB(**user_profile.__dict__)


async def update_user_profile_func(
    user_profile_id: int, user_profile_data: UserProfile, session: Session
):
    user_profile_statement = select(UserProfileTable).where(
        UserProfileTable.id == user_profile_id
    )
    user_profile = session.exec(user_profile_statement).first()

    if not user_profile:
        raise HTTPException(status_code=400, detail="User profile not found")

    for var, value in vars(user_profile_data).items():
        setattr(user_profile, var, value if value else getattr(user_profile, var))

    session.add(user_profile)
    session.commit()

    return UserProfileInDB(**user_profile.__dict__)


async def delete_user_profile_func(user_profile_id: int, session: Session):
    user_profile_statement = select(UserProfileTable).where(
        UserProfileTable.id == user_profile_id
    )
    user_profile = session.exec(user_profile_statement).first()
    if not user_profile:
        raise HTTPException(status_code=400, detail="User profile not found")

    session.delete(user_profile)
    session.commit()
    return user_profile_id
