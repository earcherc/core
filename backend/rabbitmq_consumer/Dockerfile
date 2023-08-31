# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8003 available to the world outside this container
EXPOSE 8003

# Make the shell script executable
# Note: Ensure this script is executable locally as permissions are preserved when copied into the container.
RUN chmod +x ./run.sh
RUN chmod +x ./wait-for.sh

# Introduce a delay to ensure RabbitMQ is fully initialized before this service starts
CMD ["./wait-for.sh", "rabbitmq:5672", "--", "./run.sh"]
