from fastapi import APIRouter, Depends
from ...services import forward_request, get_current_active_user
from shared_schemas.auth import TokenData
from shared_schemas.auth import UserUpdate

router = APIRouter()


@router.put("/")
async def update_user(
    user_data: UserUpdate,
    current_user: TokenData = Depends(get_current_active_user),
):
    response = await forward_request(
        method="put",
        path=f"user/{current_user.user_id}",
        params=user_data.dict(),
        service="auth",
    )
    return response
