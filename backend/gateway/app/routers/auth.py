from fastapi import APIRouter, HTTPException, Depends
from ..services import forward_request
from ..schemas import User
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()


@router.post("/register")
async def register(user: User):
    try:
        response = await forward_request(
            "auth/register", params=user.dict(), service="auth"
        )
    except HTTPException as exc:
        raise HTTPException(status_code=exc.status_code, detail=exc.detail)
    return response


@router.post("/login")
async def login(data: OAuth2PasswordRequestForm = Depends()):
    try:
        response = await forward_request(
            "auth/login", params=data.__dict__, service="auth", is_form_data=True
        )
    except HTTPException as exc:
        raise HTTPException(status_code=exc.status_code, detail=exc.detail)
    return response
