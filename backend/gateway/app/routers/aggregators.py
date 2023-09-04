from fastapi import APIRouter, Depends
from ..services import forward_request, get_current_active_user


router = APIRouter()


@router.get("/user-profile/{user_id}")
async def get_aggregated_user_profile(user_id: int):
    pass
    # return await aggregate_user_data(user_id)
