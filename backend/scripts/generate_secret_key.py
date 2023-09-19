import secrets
import base64


def generate_key():
    return base64.b64encode(secrets.token_bytes(32)).decode("utf-8")


if __name__ == "__main__":
    print(generate_key())
