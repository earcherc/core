from fastapi import FastAPI
from app.routers import core, study_block, user_profile


app = FastAPI()

app.include_router(core.router, prefix="/core", tags=["Core"])
app.include_router(study_block.router, prefix="/core/study_block", tags=["StudyBlock"])
app.include_router(
    user_profile.router, prefix="/core/user_profile", tags=["UserProfile"]
)
