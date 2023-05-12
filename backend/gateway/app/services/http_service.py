from typing import Annotated
import httpx
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from ..config import Config
from jose import JWTError, jwt
from ..schemas import User, TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def forward_request(
    path: str,
    params: dict = {},
    headers: dict = {},
    service: str = "auth",
    is_form_data: bool = False,
):
    """Forward a request to another service"""
    service_url = Config.SERVICE_URLS.get(service)
    if not service_url:
        raise HTTPException(status_code=500, detail=f"Unknown service: {service}")

    url = f"{service_url}/{path}"

    response = None
    async with httpx.AsyncClient() as client:
        try:
            if is_form_data:
                response = await client.post(url, data=params, headers=headers)
            else:
                response = await client.post(url, json=params, headers=headers)
            response.raise_for_status()
        except httpx.HTTPStatusError as http_err:
            if response:
                raise HTTPException(
                    status_code=response.status_code, detail=str(http_err)
                )
            else:
                raise HTTPException(status_code=500, detail=str(http_err))

    return response.json()


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        if Config.SECRET_KEY is None or Config.ALGORITHM is None:
            raise ValueError("Invalid configuration: missing SECRET_KEY or ALGORITHM")
        payload = jwt.decode(token, Config.SECRET_KEY, algorithms=[Config.ALGORITHM])
        username: str = payload.get("sub", "")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    return token_data


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
