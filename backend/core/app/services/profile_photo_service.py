from typing import List, Optional
from sqlmodel import Session, select
from fastapi import HTTPException
from ..models import ProfilePhoto as ProfilePhotoTable
from shared_schemas.core import ProfilePhotoCreate, ProfilePhotoUpdate, ProfilePhotoInDB


async def create_profile_photo_func(
    profile_photo_data: ProfilePhotoCreate, session: Session
) -> ProfilePhotoInDB:
    profile_photo = ProfilePhotoTable(**profile_photo_data.dict())
    session.add(profile_photo)
    session.commit()
    session.refresh(profile_photo)
    return ProfilePhotoInDB.from_orm(profile_photo)


async def get_profile_photo_func(
    profile_photo_id: int, session: Session
) -> Optional[ProfilePhotoInDB]:
    profile_photo_statement = select(ProfilePhotoTable).where(
        ProfilePhotoTable.id == profile_photo_id
    )
    profile_photo = session.exec(profile_photo_statement).first()
    if not profile_photo:
        raise HTTPException(status_code=404, detail="Profile photo not found")
    return ProfilePhotoInDB.from_orm(profile_photo)


async def get_all_profile_photos_func(session: Session) -> List[ProfilePhotoInDB]:
    profile_photo_statement = select(ProfilePhotoTable)
    profile_photos = session.exec(profile_photo_statement).all()
    return [ProfilePhotoInDB.from_orm(photo) for photo in profile_photos]


async def update_profile_photo_func(
    profile_photo_id: int, profile_photo_data: ProfilePhotoUpdate, session: Session
) -> ProfilePhotoInDB:
    profile_photo_statement = select(ProfilePhotoTable).where(
        ProfilePhotoTable.id == profile_photo_id
    )
    profile_photo = session.exec(profile_photo_statement).first()
    if not profile_photo:
        raise HTTPException(status_code=404, detail="Profile photo not found")

    for var, value in profile_photo_data.dict(exclude_unset=True).items():
        setattr(profile_photo, var, value)

    session.add(profile_photo)
    session.commit()
    session.refresh(profile_photo)
    return ProfilePhotoInDB.from_orm(profile_photo)


async def delete_profile_photo_func(profile_photo_id: int, session: Session) -> int:
    profile_photo_statement = select(ProfilePhotoTable).where(
        ProfilePhotoTable.id == profile_photo_id
    )
    profile_photo = session.exec(profile_photo_statement).first()
    if not profile_photo:
        raise HTTPException(status_code=404, detail="Profile photo not found")

    session.delete(profile_photo)
    session.commit()
    return profile_photo_id
