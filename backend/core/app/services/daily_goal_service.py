from typing import List, Optional

from fastapi import HTTPException

from ..models import DailyGoal as DailyGoalTable
from ..schemas import DailyGoal, DailyGoalInDB
from sqlmodel import Session, select


async def create_daily_goal_func(
    user_id: int, daily_goal_data: DailyGoal, session: Session
):
    daily_goal = DailyGoalTable(**daily_goal_data.dict(), user_id=user_id)
    session.add(daily_goal)
    session.commit()
    session.refresh(daily_goal)
    return DailyGoalInDB(**daily_goal.__dict__)


async def get_user_daily_goals_func(
    user_id: int, session: Session
) -> List[DailyGoalInDB]:
    statement = select(DailyGoalTable).where(DailyGoalTable.user_id == user_id)
    results = session.exec(statement).all()

    return [DailyGoalInDB(**dg.__dict__) for dg in results]


async def get_daily_goal_func(daily_goal_id: int, session: Session):
    daily_goal_statement = select(DailyGoalTable).where(
        DailyGoalTable.id == daily_goal_id
    )
    daily_goal = session.exec(daily_goal_statement).first()
    if not daily_goal:
        raise HTTPException(status_code=404, detail="Daily goal not found")
    return DailyGoalInDB(**daily_goal.__dict__)


async def get_all_daily_goals_func(session: Session) -> List[DailyGoalInDB]:
    daily_goals_statement = select(DailyGoalTable)
    daily_goals = session.exec(daily_goals_statement).all()
    return [DailyGoalInDB(**dg.__dict__) for dg in daily_goals]


async def update_daily_goal_func(
    daily_goal_id: int, daily_goal_data: DailyGoal, session: Session
):
    daily_goal_statement = select(DailyGoalTable).where(
        DailyGoalTable.id == daily_goal_id
    )
    daily_goal = session.exec(daily_goal_statement).first()
    if not daily_goal:
        raise HTTPException(status_code=404, detail="Daily goal not found")

    for key, value in daily_goal_data.dict().items():
        setattr(daily_goal, key, value)

    session.add(daily_goal)
    session.commit()
    session.refresh(daily_goal)
    return DailyGoalInDB(**daily_goal.__dict__)


async def delete_daily_goal_func(daily_goal_id: int, session: Session):
    daily_goal_statement = select(DailyGoalTable).where(
        DailyGoalTable.id == daily_goal_id
    )
    daily_goal = session.exec(daily_goal_statement).first()
    if not daily_goal:
        raise HTTPException(status_code=404, detail="Daily goal not found")

    session.delete(daily_goal)
    session.commit()

    return daily_goal_id
