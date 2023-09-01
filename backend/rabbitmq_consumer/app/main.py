# Asbolute import required for Docker to correctly import the module
from app.consumers import core_consumer
import pika


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
    channel = connection.channel()

    # Declare the queue
    channel.queue_declare(queue="user_registration")

    # Consume messages
    channel.basic_consume(
        queue="user_registration", on_message_callback=core_consumer.message_callback
    )

    print("Waiting for messages.")
    channel.start_consuming()


if __name__ == "__main__":
    main()
