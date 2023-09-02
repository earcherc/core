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
  libpq-dev \
  netcat-traditional

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME Auth

# Make the shell scripts executable
# Note: Ensure these scripts are executable locally as permissions are preserved when copied into the container.
RUN chmod +x ./run.sh
RUN chmod +x ./wait-for-db.sh

# Run the shell script when the container launches
CMD ["./wait-for-db.sh"]  