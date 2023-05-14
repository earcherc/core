from fastapi import APIRouter, Depends
from ..services import forward_request, get_current_active_user
from ..schemas.core_schemas import DailyGoalCreate, DailyGoalUpdate
from ..schemas import TokenData

router = APIRouter()


@router.post("/")
async def create_daily_goal(
    daily_goal: DailyGoalCreate,
    current_user: TokenData = Depends(get_current_active_user),
):
    response = await forward_request(
        method="post",
        path=f"daily_goal/{current_user.user_id}",
        params=daily_goal.dict(),
        service="core",
    )
    return response


@router.get("/{daily_goal_id}")
async def get_daily_goal(
    daily_goal_id: int, current_user: TokenData = Depends(get_current_active_user)
):
    response = await forward_request(
        method="get", path=f"daily_goal/{daily_goal_id}", service="core"
    )
    return response


@router.get("/")
async def get_user_daily_goals(
    current_user: TokenData = Depends(get_current_active_user),
):
    response = await forward_request(
        method="get", path=f"daily_goal/user/{current_user.user_id}", service="core"
    )
    return response


@router.put("/{daily_goal_id}")
async def update_daily_goal(
    daily_goal_id: int,
    daily_goal: DailyGoalUpdate,
    current_user: TokenData = Depends(get_current_active_user),
):
    response = await forward_request(
        method="put",
        path=f"daily_goal/{daily_goal_id}",
        params=daily_goal.dict(),
        service="core",
    )
    return response


@router.delete("/{daily_goal_id}")
async def delete_daily_goal(
    daily_goal_id: int, current_user: TokenData = Depends(get_current_active_user)
):
    response = await forward_request(
        method="delete", path=f"daily_goal/{daily_goal_id}", service="core"
    )
    return response
