from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..schemas import DailyGoal, DailyGoalInDB
from ..services.daily_goal_service import (
    create_daily_goal_func,
    get_daily_goal_func,
    get_all_daily_goals_func,
    update_daily_goal_func,
    delete_daily_goal_func,
    get_user_daily_goals_func,
)
from app import get_session

router = APIRouter()


@router.post("/{user_id}", response_model=DailyGoalInDB, status_code=201)
async def create_daily_goal(
    user_id: int, daily_goal: DailyGoal, session: Session = Depends(get_session)
):
    return await create_daily_goal_func(user_id, daily_goal, session)


@router.get("/{daily_goal_id}", response_model=DailyGoalInDB)
async def get_daily_goal(daily_goal_id: int, session: Session = Depends(get_session)):
    db_daily_goal = await get_daily_goal_func(daily_goal_id, session)
    return db_daily_goal


@router.get("/user/{user_id}", response_model=List[DailyGoalInDB])
async def get_user_daily_goals(
    user_id: int,
    session: Session = Depends(get_session),
):
    daily_goals = await get_user_daily_goals_func(user_id, session)
    return daily_goals


@router.get("/", response_model=List[DailyGoalInDB])
async def get_all_daily_goals(session: Session = Depends(get_session)):
    return await get_all_daily_goals_func(session)


@router.put("/{daily_goal_id}", response_model=DailyGoalInDB)
async def update_daily_goal(
    daily_goal_id: int, daily_goal: DailyGoal, session: Session = Depends(get_session)
):
    db_daily_goal = await update_daily_goal_func(daily_goal_id, daily_goal, session)
    return db_daily_goal


@router.delete("/{daily_goal_id}")
async def delete_daily_goal(
    daily_goal_id: int, session: Session = Depends(get_session)
):
    deleted_daily_goal_id = await delete_daily_goal_func(daily_goal_id, session)
    return {"detail": "Successfully deleted the DailyGoal"}
