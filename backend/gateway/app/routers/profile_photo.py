from fastapi import APIRouter, Depends
from ..services import forward_request, get_current_active_user
from shared_schemas.auth import TokenData
from shared_schemas.core import ProfilePhotoCreate, ProfilePhotoUpdate

router = APIRouter()


@router.post("/")
async def create_profile_photo(
    profile_photo: ProfilePhotoCreate,
    current_user: TokenData = Depends(get_current_active_user),
):
    response = await forward_request(
        method="post",
        path="profile_photo/",
        params=profile_photo.dict(),
        service="core",
    )
    return response


@router.get("/{profile_photo_id}")
async def read_profile_photo(
    profile_photo_id: int, current_user: TokenData = Depends(get_current_active_user)
):
    response = await forward_request(
        method="get", path=f"profile_photo/{profile_photo_id}", service="core"
    )
    return response


@router.get("/")
async def read_profile_photos(
    current_user: TokenData = Depends(get_current_active_user),
):
    response = await forward_request(
        method="get", path=f"profile_photo/", service="core"
    )
    return response


@router.put("/{profile_photo_id}")
async def update_profile_photo(
    profile_photo_id: int,
    profile_photo: ProfilePhotoUpdate,
    current_user: TokenData = Depends(get_current_active_user),
):
    response = await forward_request(
        method="put",
        path=f"profile_photo/{profile_photo_id}",
        params=profile_photo.dict(),
        service="core",
    )
    return response


@router.delete("/{profile_photo_id}")
async def delete_profile_photo(
    profile_photo_id: int, current_user: TokenData = Depends(get_current_active_user)
):
    response = await forward_request(
        method="delete", path=f"profile_photo/{profile_photo_id}", service="core"
    )
    return response
