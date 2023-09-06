from fastapi import HTTPException
from sqlmodel import Session, select
from ..models import User as UserTable
from shared_schemas.auth import UserInDB, UserUpdate


async def update_user_func(
    user_id: int, user_data: UserUpdate, session: Session
) -> UserInDB:
    user_statement = select(UserTable).where(UserTable.id == user_id)
    user = session.exec(user_statement).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    for var, value in user_data.dict(exclude_unset=True).items():
        if value is not None:
            setattr(user, var, value)

    session.add(user)
    session.commit()
    session.refresh(user)
    return UserInDB.from_orm(user)
