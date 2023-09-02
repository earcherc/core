from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..schemas import ProfilePhotoCreate, ProfilePhotoUpdate, ProfilePhotoInDB
from ..services.profile_photo_service import (
    create_profile_photo_func,
    get_profile_photo_func,
    update_profile_photo_func,
    delete_profile_photo_func,
)
from app import get_session

router = APIRouter(prefix="/profile-photo", tags=["Profile Photos"])


@router.post("/", response_model=ProfilePhotoInDB, status_code=201)
async def create_profile_photo(
    profile_photo: ProfilePhotoCreate,
    session: Session = Depends(get_session),
):
    db_profile_photo = await create_profile_photo_func(profile_photo, session)
    return db_profile_photo


@router.get("/{profile_photo_id}", response_model=ProfilePhotoInDB)
async def get_profile_photo(
    profile_photo_id: int,
    session: Session = Depends(get_session),
):
    db_profile_photo = await get_profile_photo_func(profile_photo_id, session)
    return db_profile_photo


@router.put("/{profile_photo_id}", response_model=ProfilePhotoInDB)
async def update_profile_photo(
    profile_photo_id: int,
    profile_photo: ProfilePhotoUpdate,
    session: Session = Depends(get_session),
):
    updated_profile_photo = await update_profile_photo_func(
        profile_photo_id, profile_photo, session
    )
    return updated_profile_photo


@router.delete("/{profile_photo_id}", status_code=204)
async def delete_profile_photo(
    profile_photo_id: int,
    session: Session = Depends(get_session),
):
    await delete_profile_photo_func(profile_photo_id, session)
    return {"message": "Profile photo deleted successfully"}
