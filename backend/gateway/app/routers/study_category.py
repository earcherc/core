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
    response = await forward_request(
        method="post",
        path="study_category/",
        params=study_category.dict(),
        service="core",
    )
    return response


@router.get("/{study_category_id}")
async def read_study_category(
    study_category_id: int, current_user: User = Depends(get_current_active_user)
):
    response = await forward_request(
        method="get", path=f"study_category/{study_category_id}", service="core"
    )
    return response


@router.put("/{study_category_id}")
async def update_study_category(
    study_category_id: int,
    study_category: StudyCategoryUpdate,
    current_user: User = Depends(get_current_active_user),
):
    response = await forward_request(
        method="put",
        path=f"study_category/{study_category_id}",
        params=study_category.dict(),
        service="core",
    )
    return response


@router.delete("/{study_category_id}")
async def delete_study_category(
    study_category_id: int, current_user: User = Depends(get_current_active_user)
):
    response = await forward_request(
        method="delete", path=f"study_category/{study_category_id}", service="core"
    )
    return response
