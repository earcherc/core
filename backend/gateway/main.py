from fastapi import FastAPI
from app.routers import auth, user_profile, study_block, daily_goal, study_category

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(user_profile.router, prefix="/user_profile", tags=["User Profile"])
app.include_router(study_block.router, prefix="/study_block", tags=["Study Block"])
app.include_router(daily_goal.router, prefix="/daily_goal", tags=["Daily Goal"])
app.include_router(
    study_category.router, prefix="/study_category", tags=["Study Category"]
)
