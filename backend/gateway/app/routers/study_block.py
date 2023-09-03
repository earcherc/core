from fastapi import APIRouter, Depends
from ..services import forward_request, get_current_active_user
from shared_schemas.core import StudyBlock, StudyBlockCreate, StudyBlockUpdate
from shared_schemas.auth import TokenData

router = APIRouter()


@router.post("/")
async def create_study_block(
    study_block: StudyBlockCreate,
    current_user: TokenData = Depends(get_current_active_user),
):
    study_block_dict = study_block.dict()
    study_block_dict["start"] = study_block.start.isoformat()
    study_block_dict["end"] = study_block.end.isoformat()
    study_block_dict["user_id"] = current_user.user_id

    response = await forward_request(
        method="post",
        path="study_block/",
        params=study_block_dict,
        service="core",
    )
    return response


@router.get("/")
async def get_user_study_blocks(
    current_user: TokenData = Depends(get_current_active_user),
):
    response = await forward_request(
        method="get", path=f"study_block/{current_user.user_id}", service="core"
    )
    return response


@router.put("/{study_block_id}")
async def update_study_block(
    study_block_id: int,
    study_block: StudyBlockUpdate,
    current_user: TokenData = Depends(get_current_active_user),
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
    study_block_id: int, current_user: TokenData = Depends(get_current_active_user)
):
    response = await forward_request(
        method="delete", path=f"study_block/{study_block_id}", service="core"
    )
    return response
