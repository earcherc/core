import httpx
import json


def message_callback(ch, method, properties, body):
    # Decode the message from RabbitMQ
    user_data = body.decode("utf-8").strip()
    print(f"Decoded message: {user_data}")

    if not user_data:
        print("Received empty message, skipping.")
        return

    try:
        user_data_dict = json.loads(user_data)
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")
        return

    print(f"JSON decoded message: {user_data_dict}")

    # Make sure "user_id" exists in the message
    if "user_id" not in user_data_dict:
        print("The message doesn't contain 'user_id', skipping.")
        return

    # Prepare the payload for the Core service
    payload = {
        "user_id": user_data_dict["user_id"],
        "favorite_color": None,
        "bio": None,
    }

    # HTTP POST request to the Core service
    core_service_url = "http://core:8001/user_profile/"

    with httpx.Client() as client:
        response = client.post(core_service_url, json=payload)

    if response.status_code != 201:
        print(
            f"Failed to create UserProfile in Core service. Status: {response.status_code}, Detail: {response.text}"
        )
        return

    print(f"Successfully created UserProfile in Core service.")
