from fastapi import APIRouter, HTTPException, Depends
from ..services import forward_request, get_current_active_user
from ..schemas.core_schemas import DailyGoal, DailyGoalCreate, DailyGoalUpdate
from ..schemas import User


router = APIRouter()


@router.post("/")
async def create_daily_goal(
    daily_goal: DailyGoalCreate, current_user: User = Depends(get_current_active_user)
):
    try:
        response = await forward_request("/", params=daily_goal.dict(), service="core")
    except HTTPException as exc:
        raise HTTPException(status_code=exc.status_code, detail=exc.detail)
    return response


@router.get("/{daily_goal_id}")
async def read_daily_goal(
    daily_goal_id: int, current_user: User = Depends(get_current_active_user)
):
    try:
        response = await forward_request(f"/{daily_goal_id}", service="core")
    except HTTPException as exc:
        raise HTTPException(status_code=exc.status_code, detail=exc.detail)
    return response


@router.put("/{daily_goal_id}")
async def update_daily_goal(
    daily_goal_id: int,
    daily_goal: DailyGoalUpdate,
    current_user: User = Depends(get_current_active_user),
):
    try:
        response = await forward_request(
            f"/{daily_goal_id}",
            params=daily_goal.dict(),
            service="core",
        )
    except HTTPException as exc:
        raise HTTPException(status_code=exc.status_code, detail=exc.detail)
    return response


@router.delete("/{daily_id}")
async def delete_daily_goal(
    daily_goal_id: int, current_user: User = Depends(get_current_active_user)
):
    try:
        response = await forward_request(f"/{daily_goal_id}", service="core")
    except HTTPException as exc:
        raise HTTPException(status_code=exc.status_code, detail=exc.detail)

    return response
