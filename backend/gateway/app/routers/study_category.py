# routers/study_category.py

from fastapi import APIRouter, HTTPException, Depends
from ..services import forward_request, get_current_active_user
from ..schemas.core_schemas import (
    StudyCategory,
    StudyCategoryCreate,
    StudyCategoryUpdate,
)
from ..schemas import User


router = APIRouter()


@router.post("/")
async def create_study_category(
    study_category: StudyCategoryCreate,
    current_user: User = Depends(get_current_active_user),
):
    try:
        response = await forward_request(
            "study-category", params=study_category.dict(), service="core"
        )
    except HTTPException as exc:
        raise HTTPException(status_code=exc.status_code, detail=exc.detail)
    return response


@router.get("/{study_category_id}")
async def read_study_category(
    study_category_id: int, current_user: User = Depends(get_current_active_user)
):
    try:
        response = await forward_request(
            f"study-category/{study_category_id}", service="core"
        )
    except HTTPException as exc:
        raise HTTPException(status_code=exc.status_code, detail=exc.detail)
    return response


@router.put("/{study_category_id}")
async def update_study_category(
    study_category_id: int,
    study_category: StudyCategoryUpdate,
    current_user: User = Depends(get_current_active_user),
):
    try:
        response = await forward_request(
            f"study-category/{study_category_id}",
            params=study_category.dict(),
            service="core",
        )
    except HTTPException as exc:
        raise HTTPException(status_code=exc.status_code, detail=exc.detail)
    return response


@router.delete("/{study_category_id}")
async def delete_study_category(
    study_category_id: int, current_user: User = Depends(get_current_active_user)
):
    try:
        response = await forward_request(
            f"study-category/{study_category_id}", service="core"
        )
    except HTTPException as exc:
        raise HTTPException(status_code=exc.status_code, detail=exc.detail)

    return response
