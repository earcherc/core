from fastapi import APIRouter


router = APIRouter()


@router.get("/", status_code=201)
async def test():
    return {"Test": "Hello world"}
