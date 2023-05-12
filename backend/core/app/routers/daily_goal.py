from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from ..schemas import DailyGoal, DailyGoalInDB
from ..services.daily_goal_service import (
    create_daily_goal,
    get_daily_goal,
    get_all_daily_goals,
    update_daily_goal,
    delete_daily_goal,
)
from app import get_session

router = APIRouter()


@router.post("/", response_model=DailyGoalInDB, status_code=201)
async def create_daily_goal_route(
    daily_goal: DailyGoal, session: Session = Depends(get_session)
):
    return await create_daily_goal(daily_goal, session)


@router.get("/{daily_goal_id}", response_model=DailyGoalInDB)
async def get_daily_goal_route(
    daily_goal_id: int, session: Session = Depends(get_session)
):
    db_daily_goal = await get_daily_goal(daily_goal_id, session)
    if not db_daily_goal:
        raise HTTPException(status_code=404, detail="DailyGoal not found")
    return db_daily_goal


@router.get("/", response_model=List[DailyGoalInDB])
async def get_all_daily_goals_route(session: Session = Depends(get_session)):
    return await get_all_daily_goals(session)


@router.put("/{daily_goal_id}", response_model=DailyGoalInDB)
async def update_daily_goal_route(
    daily_goal_id: int, daily_goal: DailyGoal, session: Session = Depends(get_session)
):
    db_daily_goal = await update_daily_goal(daily_goal_id, daily_goal, session)
    if not db_daily_goal:
        raise HTTPException(status_code=404, detail="DailyGoal not found")
    return db_daily_goal


@router.delete("/{daily_goal_id}")
async def delete_daily_goal_route(
    daily_goal_id: int, session: Session = Depends(get_session)
):
    deleted_daily_goal_id = await delete_daily_goal(daily_goal_id, session)
    if not deleted_daily_goal_id:
        raise HTTPException(status_code=404, detail="DailyGoal not found")
    return {"detail": "Successfully deleted the DailyGoal"}
