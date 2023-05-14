from fastapi import APIRouter, Depends

from ..services import forward_request, get_current_active_user
from ..schemas.auth_schemas import TokenData
from ..schemas.core_schemas import (
    StudyCategoryCreate,
    StudyCategoryUpdate,
)

router = APIRouter()


@router.post("/")
async def create_study_category(
    study_category: StudyCategoryCreate,
    current_user: TokenData = Depends(get_current_active_user),
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
    study_category_id: int, current_user: TokenData = Depends(get_current_active_user)
):
    response = await forward_request(
        method="get", path=f"study_category/{study_category_id}", service="core"
    )
    return response


@router.get("/")
async def read_study_categories(
    current_user: TokenData = Depends(get_current_active_user),
):
    response = await forward_request(
        method="get", path=f"study_category/", service="core"
    )
    return response


@router.put("/{study_category_id}")
async def update_study_category(
    study_category_id: int,
    study_category: StudyCategoryUpdate,
    current_user: TokenData = Depends(get_current_active_user),
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
    study_category_id: int, current_user: TokenData = Depends(get_current_active_user)
):
    response = await forward_request(
        method="delete", path=f"study_category/{study_category_id}", service="core"
    )
    return response
