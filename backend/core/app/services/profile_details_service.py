from typing import Optional
from ..models import UserProfileDetails as UserProfileDetailsTable
from shared_schemas.core import (
    UserProfileDetailsInDB,
    UserProfileDetailsCreate,
    UserProfileDetailsUpdate,
)
from sqlmodel import Session, select
from fastapi import HTTPException


async def get_profile_details_func(
    user_profile_id: int, session: Session
) -> Optional[UserProfileDetailsInDB]:
    user_profile_details_statement = select(UserProfileDetailsTable).where(
        UserProfileDetailsTable.user_profile_id == user_profile_id
    )
    user_profile_details = session.exec(user_profile_details_statement).first()
    if not user_profile_details:
        raise HTTPException(status_code=404, detail="User profile details not found")

    return UserProfileDetailsInDB.from_orm(user_profile_details)


async def create_profile_details_func(
    user_profile_details_data: UserProfileDetailsCreate, session: Session
):
    existing_profile_details = session.exec(
        select(UserProfileDetailsTable).where(
            UserProfileDetailsTable.user_profile_id
            == user_profile_details_data.user_profile_id
        )
    ).first()

    if existing_profile_details is not None:
        raise HTTPException(
            status_code=400,
            detail="User profile details for this user_profile_id already exist",
        )

    user_profile_details = UserProfileDetailsTable(**user_profile_details_data.dict())

    session.add(user_profile_details)
    session.commit()
    session.refresh(user_profile_details)

    return UserProfileDetailsInDB.from_orm(user_profile_details)


async def update_profile_details_func(
    user_profile_id: int,
    user_profile_details_data: UserProfileDetailsUpdate,
    session: Session,
):
    user_profile_details_statement = select(UserProfileDetailsTable).where(
        UserProfileDetailsTable.user_profile_id == user_profile_id
    )
    user_profile_details = session.exec(user_profile_details_statement).first()

    if not user_profile_details:
        raise HTTPException(status_code=404, detail="User profile details not found")

    # Only update fields that are set
    for var, value in user_profile_details_data.dict(exclude_unset=True).items():
        setattr(user_profile_details, var, value)

    session.add(user_profile_details)
    session.commit()
    session.refresh(user_profile_details)

    return UserProfileDetailsInDB.from_orm(user_profile_details)


async def delete_profile_details_func(user_profile_id: int, session: Session):
    user_profile_details_statement = select(UserProfileDetailsTable).where(
        UserProfileDetailsTable.user_profile_id == user_profile_id
    )
    user_profile_details = session.exec(user_profile_details_statement).first()
    if not user_profile_details:
        raise HTTPException(status_code=404, detail="User profile details not found")

    session.delete(user_profile_details)
    session.commit()
    return user_profile_id
