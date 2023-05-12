from fastapi import FastAPI
from app.routers import gateway

app = FastAPI()

app.include_router(gateway.router, prefix="/gateway", tags=["gateway"])
