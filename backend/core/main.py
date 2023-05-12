from fastapi import FastAPI
from app.routers import core


app = FastAPI()

app.include_router(core.router, prefix="/core", tags=["Core"])
