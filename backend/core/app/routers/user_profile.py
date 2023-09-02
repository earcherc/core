from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..schemas import UserProfileCreate, UserProfileUpdate, UserProfileInDB
from ..services.user_profile_service import (
    create_user_profile_func,
    get_user_profile_func,
    update_user_profile_func,
    delete_user_profile_func,
)
from app import get_session

router = APIRouter()


@router.post("/", response_model=UserProfileInDB, status_code=201)
async def create_user_profile(
    user_profile: UserProfileCreate,
    session: Session = Depends(get_session),
):
    db_user_profile = await create_user_profile_func(user_profile, session)
    return db_user_profile


@router.get("/{user_id}", response_model=UserProfileInDB)
async def get_user_profile(
    user_id: int,
    session: Session = Depends(get_session),
):
    db_user_profile = await get_user_profile_func(user_id, session)
    return db_user_profile


@router.put("/{user_id}", response_model=UserProfileInDB)
async def update_user_profile(
    user_id: int,
    user_profile: UserProfileUpdate,
    session: Session = Depends(get_session),
):
    updated_user_profile = await update_user_profile_func(
        user_id, user_profile, session
    )
    return updated_user_profile


@router.delete("/{user_id}", status_code=204)
async def delete_user_profile(
    user_id: int,
    session: Session = Depends(get_session),
):
    await delete_user_profile_func(user_id, session)
    return {"message": "User profile deleted successfully"}
