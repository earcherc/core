from fastapi import APIRouter, HTTPException, Depends
from ..services import forward_request, get_current_active_user
from ..schemas import UserProfile, TokenData, UserProfileCreate
from ..schemas import User


router = APIRouter()


@router.post("/")
async def create_user_profile(
    user_profile: UserProfileCreate,
    current_user: TokenData = Depends(get_current_active_user),
):
    if current_user.user_id:
        user_profile.user_id = current_user.user_id

    response = await forward_request(
        "user_profile/", params=user_profile.dict(), service="core"
    )
    return response


@router.get("/{user_profile_id}")
async def read_user_profile(
    user_profile_id: int, current_user: User = Depends(get_current_active_user)
):
    response = await forward_request(f"user_profile/{user_profile_id}", service="core")
    return response


@router.put("/{user_profile_id}")
async def update_user_profile(
    user_profile_id: int,
    user_profile: UserProfile,
    current_user: User = Depends(get_current_active_user),
):
    response = await forward_request(
        f"user_profile/{user_profile_id}",
        params=user_profile.dict(),
        service="core",
    )
    return response


@router.delete("/{user_profile_id}")
async def delete_user_profile(
    user_profile_id: int, current_user: User = Depends(get_current_active_user)
):
    response = await forward_request(f"user_profile/{user_profile_id}", service="core")

    return response
