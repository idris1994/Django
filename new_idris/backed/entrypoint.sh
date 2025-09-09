#!/usr/bin/env bash
set -e

# Wait for Postgres
if [ -n "$POSTGRES_HOST" ]; then
  until nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
    echo "Waiting for postgres at $POSTGRES_HOST:$POSTGRES_PORT..."
    sleep 1
  done
fi

python manage.py collectstatic --noinput || true
python manage.py migrate --noinput
python manage.py runserver 0.0.0.0:8000
