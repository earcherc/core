from fastapi import APIRouter, HTTPException, Depends
from ..services import forward_request, get_current_active_user
from ..schemas.core_schemas import StudyBlock, StudyBlockCreate, StudyBlockUpdate
from ..schemas import User

router = APIRouter()


@router.post("/")
async def create_study_block(
    study_block: StudyBlockCreate, current_user: User = Depends(get_current_active_user)
):
    response = await forward_request(
        method="post", path="study_block/", params=study_block.dict(), service="core"
    )
    return response


@router.get("/{study_block_id}")
async def read_study_block(
    study_block_id: int, current_user: User = Depends(get_current_active_user)
):
    response = await forward_request(
        method="get", path=f"study_block/{study_block_id}", service="core"
    )
    return response


@router.put("/{study_block_id}")
async def update_study_block(
    study_block_id: int,
    study_block: StudyBlockUpdate,
    current_user: User = Depends(get_current_active_user),
):
    response = await forward_request(
        method="put",
        path=f"study_block/{study_block_id}",
        params=study_block.dict(),
        service="core",
    )
    return response


@router.delete("/{study_block_id}")
async def delete_study_block(
    study_block_id: int, current_user: User = Depends(get_current_active_user)
):
    response = await forward_request(
        method="delete", path=f"study_block/{study_block_id}", service="core"
    )
    return response
