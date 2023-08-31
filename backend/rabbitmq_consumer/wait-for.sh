#!/bin/sh
set -e

echo "Waiting for RabbitMQ connection"

# Loop until RabbitMQ is available
while ! nc -z rabbitmq 5672; do
    sleep 1
done

echo "RabbitMQ is up - executing command"

# Execute the remaining command
exec "./run.sh"
