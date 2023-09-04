from fastapi import APIRouter, Depends, HTTPException, status
from ..services import forward_request, get_current_active_user
from shared_schemas.auth import TokenData

router = APIRouter()


@router.get("/aggregated-profile/{user_id}")
async def get_aggregated_profile(
    user_id: int, current_user: TokenData = Depends(get_current_active_user)
):
    user_data = None
    profile_data = None

    try:
        # Forward the user request to the user service
        user_data = await forward_request(
            method="get", path=f"auth/user-info/{user_id}", service="auth"
        )
    except HTTPException as e:
        # Handle exception for the user service
        raise HTTPException(
            status_code=e.status_code,
            detail=f"Error fetching user data: {e.detail}",
        )

    try:
        # Forward the profile request to the profile service
        profile_data = await forward_request(
            method="get", path=f"user-profile/{user_id}", service="core"
        )
    except HTTPException as e:
        # Handle exception for the profile service
        raise HTTPException(
            status_code=e.status_code,
            detail=f"Error fetching profile data: {e.detail}",
        )

    # Return the aggregated data
    return {"user": user_data, "profile": profile_data}
