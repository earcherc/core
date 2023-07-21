from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader
from ..config import Config

api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)


def check_permission(
    api_key_header: str = Security(api_key_header),
):
    """Retrieve & validate an API key from the HTTP header"""

    if not Config.API_KEY:
        raise HTTPException(
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            detail="API key is not configured",
        )

    # If the API Key is is in the header and valid, return it
    if api_key_header == Config.API_KEY:
        return True

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing API Key",
    )
