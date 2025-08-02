#!/bin/bash

# Use the full Kubernetes DNS name for the database
POSTGRES_HOST="${POSTGRES_SERVICE_HOST:-postgres-service.default.svc.cluster.local}"
POSTGRES_PORT="${POSTGRES_SERVICE_PORT:-5432}"

echo "Waiting for PostgreSQL at ${POSTGRES_HOST}:${POSTGRES_PORT}..."
while ! nc -z "${POSTGRES_HOST}" "${POSTGRES_PORT}"; do
  sleep 0.5
done
echo "PostgreSQL is ready!"

## Wait for database to be ready
#echo "Waiting for database..."
#while ! nc -z $DB_HOST $DB_PORT; do
#  sleep 0.1
#done
#echo "Database started"

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start server
echo "Starting server..."
exec gunicorn --bind 0.0.0.0:8000 --workers 3 --threads 2 --timeout 120 project.wsgi:application
