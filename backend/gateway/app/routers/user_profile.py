from fastapi import APIRouter, HTTPException, Depends
from ..services import forward_request, get_current_active_user
from ..schemas import UserProfile, TokenData, UserProfileCreate

router = APIRouter()


@router.get("/")
async def read_user_profile(current_user: TokenData = Depends(get_current_active_user)):
    response = await forward_request(
        method="get", path=f"user_profile/{current_user.user_id}", service="core"
    )
    return response


@router.post("/")
async def create_user_profile(
    user_profile: UserProfileCreate,
    current_user: TokenData = Depends(get_current_active_user),
):
    user_profile.user_id = current_user.user_id

    response = await forward_request(
        method="post",
        path="user_profile/",
        params=user_profile.dict(),
        service="core",
    )
    return response


@router.put("/")
async def update_user_profile(
    user_profile: UserProfile,
    current_user: TokenData = Depends(get_current_active_user),
):
    response = await forward_request(
        method="put",
        path=f"user_profile/{current_user.user_id}",
        params=user_profile.dict(),
        service="core",
    )
    return response


@router.delete("/")
async def delete_user_profile(
    current_user: TokenData = Depends(get_current_active_user),
):
    response = await forward_request(
        method="delete", path=f"user_profile/{current_user.user_id}", service="core"
    )

    return response
