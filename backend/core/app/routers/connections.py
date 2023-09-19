from fastapi import APIRouter, Depends
from sqlmodel import Session
from shared_schemas.core import ConnectionCreate, ConnectionUpdate, ConnectionInDB
from ..services.connection_service import (
    create_connection_func,
    get_connection_func,
    update_connection_func,
    delete_connection_func,
)
from app import get_session

router = APIRouter(prefix="/connections", tags=["Connections"])


@router.post("/", response_model=ConnectionInDB, status_code=201)
async def create_connection(
    connection: ConnectionCreate,
    session: Session = Depends(get_session),
):
    db_connection = await create_connection_func(connection, session)
    return db_connection


@router.get("/{connection_id}", response_model=ConnectionInDB)
async def get_connection(
    connection_id: int,
    session: Session = Depends(get_session),
):
    db_connection = await get_connection_func(connection_id, session)
    return db_connection


@router.put("/{connection_id}", response_model=ConnectionInDB)
async def update_connection(
    connection_id: int,
    connection: ConnectionUpdate,
    session: Session = Depends(get_session),
):
    updated_connection = await update_connection_func(
        connection_id, connection, session
    )
    return updated_connection


@router.delete("/{connection_id}", status_code=204)
async def delete_connection(
    connection_id: int,
    session: Session = Depends(get_session),
):
    await delete_connection_func(connection_id, session)
    return {"message": "Connection deleted successfully"}
