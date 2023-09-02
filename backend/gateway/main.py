from fastapi import FastAPI, Depends
from app.middleware import check_permission
from app.routers import auth, user_profile, study_block, daily_goal, study_category

app = FastAPI(dependencies=[Depends(check_permission)])


app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(user_profile.router, prefix="/user-profile", tags=["User Profile"])
app.include_router(study_block.router, prefix="/study-block", tags=["Study Block"])
app.include_router(daily_goal.router, prefix="/daily-goal", tags=["Daily Goal"])
app.include_router(
    study_category.router, prefix="/study-category", tags=["Study Category"]
)
