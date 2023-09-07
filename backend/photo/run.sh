#!/bin/sh
set -e

# Run alembic migrations
alembic upgrade head

# Start the application
uvicorn main:app --host 0.0.0.0 --port 8001 --reload