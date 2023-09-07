from fastapi import FastAPI
from app.routers import connections, profile_details, profile_photo, user_profile

app = FastAPI()

app.include_router(user_profile.router, prefix="/user-profile", tags=["User Profiles"])
app.include_router(
    profile_details.router, prefix="/profile-details", tags=["Profile Details"]
)
app.include_router(connections.router, prefix="/connections", tags=["Connections"])
app.include_router(
    profile_photo.router, prefix="/profile-photo", tags=["Profile Photos"]
)
