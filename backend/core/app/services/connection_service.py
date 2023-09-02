from typing import List, Optional
from sqlmodel import Session, select
from fastapi import HTTPException
from ..models import Connection as ConnectionTable
from ..schemas import ConnectionCreate, ConnectionUpdate, ConnectionInDB


async def create_connection_func(
    connection_data: ConnectionCreate, session: Session
) -> ConnectionInDB:
    connection = ConnectionTable(**connection_data.dict())
    session.add(connection)
    session.commit()
    session.refresh(connection)
    return ConnectionInDB.from_orm(connection)


async def get_connection_func(
    connection_id: int, session: Session
) -> Optional[ConnectionInDB]:
    connection_statement = select(ConnectionTable).where(
        ConnectionTable.id == connection_id
    )
    connection = session.exec(connection_statement).first()
    if not connection:
        raise HTTPException(status_code=404, detail="Connection not found")
    return ConnectionInDB.from_orm(connection)


async def get_all_connections_func(session: Session) -> List[ConnectionInDB]:
    connection_statement = select(ConnectionTable)
    connections = session.exec(connection_statement).all()
    return [ConnectionInDB.from_orm(conn) for conn in connections]


async def update_connection_func(
    connection_id: int, connection_data: ConnectionUpdate, session: Session
) -> ConnectionInDB:
    connection_statement = select(ConnectionTable).where(
        ConnectionTable.id == connection_id
    )
    connection = session.exec(connection_statement).first()
    if not connection:
        raise HTTPException(status_code=404, detail="Connection not found")

    for var, value in connection_data.dict(exclude_unset=True).items():
        setattr(connection, var, value)

    session.add(connection)
    session.commit()
    session.refresh(connection)
    return ConnectionInDB.from_orm(connection)


async def delete_connection_func(connection_id: int, session: Session) -> int:
    connection_statement = select(ConnectionTable).where(
        ConnectionTable.id == connection_id
    )
    connection = session.exec(connection_statement).first()
    if not connection:
        raise HTTPException(status_code=404, detail="Connection not found")

    session.delete(connection)
    session.commit()
    return connection_id
