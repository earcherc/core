from fastapi import APIRouter, Depends
from ...services import forward_request
from shared_schemas.auth import UserCreate
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter()


@router.post("/register")
async def register(user: UserCreate):
    response = await forward_request(
        method="post", path="auth/register", params=user.dict(), service="auth"
    )
    return response


@router.post("/login")
async def login(data: OAuth2PasswordRequestForm = Depends()):
    response = await forward_request(
        method="post",
        path="auth/login",
        params=data.__dict__,
        service="auth",
        is_form_data=True,
    )
    return response
