from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..schemas import StudyBlockCreate, StudyBlockUpdate
from ..services import *
from app import get_session

router = APIRouter()


@router.post("/", status_code=201)
async def create_study_block(
    study_block: StudyBlockCreate, session: Session = Depends(get_session)
):
    study_block_id = await create_study_block_func(study_block, session)
    return {"study_block_id": study_block_id}


@router.get("/{study_block_id}")
async def read_study_block(
    study_block_id: int, session: Session = Depends(get_session)
):
    study_block = get_study_block_func(study_block_id, session)
    return study_block


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
    return {"detail": "StudyBlock deleted successfully"}
