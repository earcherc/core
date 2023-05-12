from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from ..schemas import StudyCategory, StudyCategoryInDB
from ..services import (
    get_all_study_categories,
    create_study_category,
    update_study_category,
    delete_study_category,
)
from app import get_session


router = APIRouter()


@router.get("/", response_model=List[StudyCategoryInDB])
async def read_study_categories(session: Session = Depends(get_session)):
    return await get_all_study_categories(session)


@router.post("/", response_model=StudyCategoryInDB)
async def create_study_category_endpoint(
    study_category: StudyCategory, session: Session = Depends(get_session)
):
    return await create_study_category(study_category, session)


@router.put("/{study_category_id}", response_model=StudyCategoryInDB)
async def update_study_category_endpoint(
    study_category_id: int,
    study_category: StudyCategory,
    session: Session = Depends(get_session),
):
    updated_study_category = await update_study_category(
        study_category_id, study_category, session
    )
    if not updated_study_category:
        raise HTTPException(status_code=404, detail="Study category not found")
    return updated_study_category


@router.delete("/{study_category_id}")
async def delete_study_category_endpoint(
    study_category_id: int, session: Session = Depends(get_session)
):
    deleted_study_category_id = await delete_study_category(study_category_id, session)
    if not deleted_study_category_id:
        raise HTTPException(status_code=404, detail="Study category not found")
    return {
        "message": f"Successfully deleted study category with id: {deleted_study_category_id}"
    }
