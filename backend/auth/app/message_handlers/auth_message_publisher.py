import pika


def publish_to_queue(message):
    # ConnectionParameters(hostname, **kwargs) hostname defined in docker-compose
    connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
    channel = connection.channel()

    channel.queue_declare(queue="user_registration")

    channel.basic_publish(exchange="", routing_key="user_registration", body=message)

    connection.close()
