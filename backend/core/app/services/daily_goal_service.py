from typing import List, Optional
from ..models import DailyGoal as DailyGoalTable
from ..schemas import DailyGoal, DailyGoalInDB
from sqlmodel import Session, select


async def create_daily_goal(daily_goal_data: DailyGoal, session: Session):
    daily_goal = DailyGoalTable(**daily_goal_data.dict())
    session.add(daily_goal)
    session.commit()
    session.refresh(daily_goal)
    return DailyGoalInDB(**daily_goal.__dict__)


async def get_daily_goal(daily_goal_id: int, session: Session):
    daily_goal_statement = select(DailyGoalTable).where(
        DailyGoalTable.id == daily_goal_id
    )
    daily_goal = session.exec(daily_goal_statement).first()
    if daily_goal:
        return DailyGoalInDB(**daily_goal.__dict__)
    return None


async def get_all_daily_goals(session: Session) -> List[DailyGoalInDB]:
    daily_goals_statement = select(DailyGoalTable)
    daily_goals = session.exec(daily_goals_statement).all()
    return [DailyGoalInDB(**dg.__dict__) for dg in daily_goals]


async def update_daily_goal(
    daily_goal_id: int, daily_goal_data: DailyGoal, session: Session
):
    daily_goal_statement = select(DailyGoalTable).where(
        DailyGoalTable.id == daily_goal_id
    )
    daily_goal = session.exec(daily_goal_statement).first()
    if not daily_goal:
        return None

    for key, value in daily_goal_data.dict().items():
        setattr(daily_goal, key, value)

    session.add(daily_goal)
    session.commit()
    session.refresh(daily_goal)
    return DailyGoalInDB(**daily_goal.__dict__)


async def delete_daily_goal(daily_goal_id: int, session: Session):
    daily_goal_statement = select(DailyGoalTable).where(
        DailyGoalTable.id == daily_goal_id
    )
    daily_goal = session.exec(daily_goal_statement).first()
    if not daily_goal:
        return None

    # Note that we don't need to assign the delete statement to a variable here.
    session.delete(daily_goal)
    session.commit()

    return daily_goal_id
