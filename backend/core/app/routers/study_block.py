from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.schemas.schemas import StudyBlockInDB
from ..schemas import StudyBlockCreate, StudyBlockUpdate
from ..services import *
from app import get_session

router = APIRouter()


@router.post("/", response_model=StudyBlockInDB, status_code=201)
async def create_study_block(
    study_block: StudyBlockCreate, session: Session = Depends(get_session)
):
    new_study_block = await create_study_block_func(study_block, session)
    return new_study_block


@router.get("/{user_id}", response_model=List[StudyBlockInDB])
async def get_user_study_blocks(
    user_id: int,
    session: Session = Depends(get_session),
):
    study_blocks = await get_user_study_blocks_func(user_id, session)
    return study_blocks


@router.put("/{study_block_id}")
async def update_study_block(
    study_block_id: int,
    study_block: StudyBlockUpdate,
    session: Session = Depends(get_session),
):
    updated_study_block = await update_study_block_func(
        study_block_id, study_block, session
    )
    return updated_study_block


@router.delete("/{study_block_id}", status_code=204)
async def delete_study_block(
    study_block_id: int, session: Session = Depends(get_session)
):
    deleted_id = await delete_study_block_func(study_block_id, session)
    return {"study_block_id": deleted_id}
