from fastapi import APIRouter, Depends
from ...services import forward_request, get_current_active_user
from shared_schemas.core import ConnectionCreate, ConnectionUpdate
from shared_schemas.auth import TokenData

router = APIRouter()


# Create new connection
@router.post("/")
async def create_connection(
    connection: ConnectionCreate,
    current_user: TokenData = Depends(get_current_active_user),
):
    response = await forward_request(
        method="post",
        path=f"connection/",
        params=connection.dict(),
        service="core",
    )
    return response


# Get specific connection by ID
@router.get("/{connection_id}")
async def get_connection(
    connection_id: int,
    current_user: TokenData = Depends(get_current_active_user),
):
    response = await forward_request(
        method="get",
        path=f"connection/{connection_id}",
        service="core",
    )
    return response


# Update a specific connection by ID
@router.put("/{connection_id}")
async def update_connection(
    connection_id: int,
    connection: ConnectionUpdate,
    current_user: TokenData = Depends(get_current_active_user),
):
    response = await forward_request(
        method="put",
        path=f"connection/{connection_id}",
        params=connection.dict(),
        service="core",
    )
    return response


# Delete a specific connection by ID
@router.delete("/{connection_id}")
async def delete_connection(
    connection_id: int,
    current_user: TokenData = Depends(get_current_active_user),
):
    response = await forward_request(
        method="delete",
        path=f"connection/{connection_id}",
        service="core",
    )
    return response
