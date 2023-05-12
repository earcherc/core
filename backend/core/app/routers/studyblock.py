from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from ..schemas import StudyBlockCreate, StudyBlockUpdate
from ..services import *
from app import get_session

router = APIRouter()


@router.post("/studyblock", status_code=201)
async def create_studyblock(
    study_block: StudyBlockCreate, session: Session = Depends(get_session)
):
    study_block_id = await create_study_block(study_block, session)

    if not study_block_id:
        raise HTTPException(status_code=400, detail="StudyBlock creation failed")

    return {"study_block_id": study_block_id}


@router.get("/studyblock/{study_block_id}")
async def read_studyblock(study_block_id: int, session: Session = Depends(get_session)):
    study_block = get_study_block(study_block_id, session)

    if not study_block:
        raise HTTPException(status_code=404, detail="StudyBlock not found")

    return study_block


@router.put("/studyblock/{study_block_id}")
async def update_studyblock(
    study_block_id: int,
    study_block: StudyBlockUpdate,
    session: Session = Depends(get_session),
):
    updated_study_block = await update_study_block(study_block_id, study_block, session)

    if not updated_study_block:
        raise HTTPException(status_code=404, detail="StudyBlock not found")

    return updated_study_block


@router.delete("/studyblock/{study_block_id}", status_code=204)
async def delete_studyblock(
    study_block_id: int, session: Session = Depends(get_session)
):
    deleted_id = await delete_study_block(study_block_id, session)

    if not deleted_id:
        raise HTTPException(status_code=404, detail="StudyBlock not found")

    return {"detail": "StudyBlock deleted successfully"}
