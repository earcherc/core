import socket


def check_connection(host, port):
    try:
        # create a socket object
        s = socket.create_connection((host, port), timeout=5)
    except OSError as err:
        print(f"Connection to {host}:{port} failed: {err}")
        return False
    else:
        s.close()
        print(f"Connection to {host}:{port} succeeded")
        return True


# Check connection to RabbitMQ
check_connection("rabbitmq", 5672)
