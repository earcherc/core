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
  libpq-dev

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8002 available to the world outside this container
EXPOSE 8002

# Define environment variable
ENV NAME Gateway

# Run main.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "debug", "--reload"]
