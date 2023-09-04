from ..services import fetch_from_auth_service, fetch_from_core_service


async def aggregate_user_data(user_id: int):
    auth_data = await fetch_from_auth_service(user_id)
    core_data = await fetch_from_core_service(user_id)

    # Merge and return
    aggregated_data = {**auth_data, **core_data}
    return aggregated_data
