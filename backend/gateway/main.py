from fastapi import FastAPI, Depends
from app.middleware import check_permission
from app.routers import (
    connection,
    profile_detail,
    profile_photo,
    user_profile,
)
from app.routers import aggregator
from app.routers import auth, user

app = FastAPI(dependencies=[Depends(check_permission)])


app.include_router(auth.router, prefix="/auth", tags=["Auth"])

app.include_router(user.router, prefix="/user", tags=["User"])

app.include_router(user_profile.router, prefix="/user-profile", tags=["User Profile"])

app.include_router(
    profile_detail.router, prefix="/user-profile-details", tags=["User Profile Details"]
)

app.include_router(connection.router, prefix="/connection", tags=["Connection"])

app.include_router(
    profile_photo.router, prefix="/profile-photo", tags=["Profile Photo"]
)

app.include_router(aggregator.router, prefix="/aggregator", tags=["Aggregator"])
