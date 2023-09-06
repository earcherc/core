from fastapi import FastAPI
from app.routers import auth, user


app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])

app.include_router(user.router, prefix="/user", tags=["User"])
