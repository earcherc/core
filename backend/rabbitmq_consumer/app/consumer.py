# app/consumer.py
import pika


def message_callback(ch, method, properties, body):
    print(f"Received message: {body}")


connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
channel = connection.channel()
channel.queue_declare(queue="some_queue")

channel.basic_consume(queue="some_queue", on_message_callback=message_callback)

print("Waiting for messages.")
channel.start_consuming()
