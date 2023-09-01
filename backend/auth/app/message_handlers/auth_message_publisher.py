import pika
import json


def publish_to_queue(message_dict):
    # Serialize Python dictionary to JSON
    json_message = json.dumps(message_dict)

    # Connect to RabbitMQ and publish the message
    connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
    channel = connection.channel()
    channel.queue_declare(queue="user_registration")
    channel.basic_publish(
        exchange="", routing_key="user_registration", body=json_message
    )

    connection.close()
