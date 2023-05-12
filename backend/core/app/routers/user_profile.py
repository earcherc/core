from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from ..schemas import UserProfile, UserProfileInDB
from ..services import *
from app import get_session

router = APIRouter()


@router.post("/user-profile", response_model=UserProfileInDB, status_code=201)
async def create_user_profile(
    user_profile: UserProfile, session: Session = Depends(get_session)
):
    db_user_profile = await create_user_profile(user_profile, session)
    if not db_user_profile:
        raise HTTPException(status_code=400, detail="User profile creation failed")
    return db_user_profile


@router.get("/user-profile/{user_id}", response_model=UserProfileInDB)
async def get_user_profile(user_id: int, session: Session = Depends(get_session)):
    db_user_profile = await get_user_profile(user_id, session)
    if not db_user_profile:
        raise HTTPException(status_code=404, detail="User profile not found")
    return db_user_profile


@router.put("/user-profile/{user_profile_id}", status_code=200)
async def update_user_profile(
    user_profile_id: int,
    user_profile: UserProfile,
    session: Session = Depends(get_session),
):
    updated_user_profile_id = await update_user_profile(
        user_profile_id, user_profile, session
    )
    if not updated_user_profile_id:
        raise HTTPException(status_code=404, detail="User profile not found")
    return {"user_profile_id": updated_user_profile_id}


@router.delete("/user-profile/{user_profile_id}", status_code=200)
async def delete_user_profile(
    user_profile_id: int, session: Session = Depends(get_session)
):
    deleted_user_profile_id = await delete_user_profile(user_profile_id, session)
    if not deleted_user_profile_id:
        raise HTTPException(status_code=404, detail="User profile not found")
    return {"user_profile_id": deleted_user_profile_id}
