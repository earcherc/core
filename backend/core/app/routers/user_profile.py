from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..schemas import UserProfile, UserProfileInDB, UserProfileCreate
from ..services import *
from app import get_session

router = APIRouter()


@router.post("/", response_model=UserProfileInDB, status_code=201)
async def create_user_profile(
    user_profile: UserProfileCreate, session: Session = Depends(get_session)
):
    db_user_profile = await create_user_profile_func(user_profile, session)
    return db_user_profile


@router.get("/{user_id}", response_model=UserProfileInDB)
async def get_user_profile(user_id: int, session: Session = Depends(get_session)):
    db_user_profile = await get_user_profile_func(user_id, session)
    return db_user_profile


@router.put("/{user_id}", response_model=UserProfileInDB, status_code=200)
async def update_user_profile(
    user_id: int,
    user_profile: UserProfile,
    session: Session = Depends(get_session),
):
    updated_user_profile_id = await update_user_profile_func(
        user_id, user_profile, session
    )
    return updated_user_profile_id


@router.delete("/{user_id}", status_code=200)
async def delete_user_profile(user_id: int, session: Session = Depends(get_session)):
    deleted_user_profile_id = await delete_user_profile_func(user_id, session)
    return {"user_profile_id": deleted_user_profile_id}
