# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install libpq-dev for psycopg2 python package
RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  gcc \
  build-essential \
  libpq-dev

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8001 available to the world outside this container
EXPOSE 8001

# Define environment variable
ENV NAME Core

# Make the shell script executable
# Note: Ensure this script is executable locally as permissions are preserved when copied into the container.
RUN chmod +x ./run.sh

# Run the shell script when the container launches
CMD ["./run.sh"]