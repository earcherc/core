from fastapi import APIRouter, Depends
from sqlmodel import Session
from shared_schemas.core import (
    UserProfileDetailsCreate,
    UserProfileDetailsUpdate,
    UserProfileDetailsInDB,
)
from ..services.profile_details_service import (
    create_profile_details_func,
    get_profile_details_func,
    update_profile_details_func,
    delete_profile_details_func,
)
from app import get_session

router = APIRouter(prefix="/profile-details", tags=["Profile Details"])


@router.post("/", response_model=UserProfileDetailsInDB, status_code=201)
async def create_profile_details(
    profile_details: UserProfileDetailsCreate,
    session: Session = Depends(get_session),
):
    db_profile_details = await create_profile_details_func(profile_details, session)
    return db_profile_details


@router.get("/{user_profile_id}", response_model=UserProfileDetailsInDB)
async def get_profile_details(
    user_profile_id: int,
    session: Session = Depends(get_session),
):
    db_profile_details = await get_profile_details_func(user_profile_id, session)
    return db_profile_details


@router.put("/{user_profile_id}", response_model=UserProfileDetailsInDB)
async def update_profile_details(
    user_profile_id: int,
    profile_details: UserProfileDetailsUpdate,
    session: Session = Depends(get_session),
):
    updated_profile_details = await update_profile_details_func(
        user_profile_id, profile_details, session
    )
    return updated_profile_details


@router.delete("/{user_profile_id}", status_code=204)
async def delete_profile_details(
    user_profile_id: int,
    session: Session = Depends(get_session),
):
    await delete_profile_details_func(user_profile_id, session)
    return {"message": "Profile details deleted successfully"}
