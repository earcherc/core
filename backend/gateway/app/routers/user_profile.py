from fastapi import APIRouter, HTTPException, Depends
from ..services import forward_request, get_current_active_user
from ..schemas.core_schemas import UserProfile
from ..schemas import User


router = APIRouter()


@router.post("/")
async def create_user_profile(
    user_profile: UserProfile, current_user: User = Depends(get_current_active_user)
):
    try:
        response = await forward_request(
            "user-profile", params=user_profile.dict(), service="core"
        )
    except HTTPException as exc:
        raise HTTPException(status_code=exc.status_code, detail=exc.detail)
    return response


@router.get("/{user_profile_id}")
async def read_user_profile(
    user_profile_id: int, current_user: User = Depends(get_current_active_user)
):
    try:
        response = await forward_request(
            f"user-profile/{user_profile_id}", service="core"
        )
    except HTTPException as exc:
        raise HTTPException(status_code=exc.status_code, detail=exc.detail)
    return response


@router.put("/{user_profile_id}")
async def update_user_profile(
    user_profile_id: int,
    user_profile: UserProfile,
    current_user: User = Depends(get_current_active_user),
):
    try:
        response = await forward_request(
            f"user-profile/{user_profile_id}",
            params=user_profile.dict(),
            service="core",
        )
    except HTTPException as exc:
        raise HTTPException(status_code=exc.status_code, detail=exc.detail)
    return response


@router.delete("/{user_profile_id}")
async def delete_user_profile(
    user_profile_id: int, current_user: User = Depends(get_current_active_user)
):
    try:
        response = await forward_request(
            f"user-profile/{user_profile_id}", service="core"
        )
    except HTTPException as exc:
        raise HTTPException(status_code=exc.status_code, detail=exc.detail)

    return response
