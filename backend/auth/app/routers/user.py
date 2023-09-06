from fastapi import APIRouter, HTTPException, Depends, status
from sqlmodel import Session
from ..services.user_service import update_user_func
from ..models import User as UserTable
from shared_schemas import User, UserUpdate, UserInDB

from app import get_session


router = APIRouter()


@router.get("/{user_id}", response_model=User)
async def get_user_info(user_id: int, session: Session = Depends(get_session)):
    user = UserTable.get_or_none(session, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user


@router.put("/{user_id}", response_model=UserInDB)
async def update_user_info(
    user_id: int, user_data: UserUpdate, session: Session = Depends(get_session)
):
    updated_user = await update_user_func(user_id, user_data, session)
    return updated_user
