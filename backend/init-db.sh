#!/bin/bash
set -e

# Use environment variables for sensitive data and database names
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE DATABASE "$DATABASE_NAME_AUTH";
    CREATE DATABASE "$DATABASE_NAME_CORE";
EOSQL