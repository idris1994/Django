# Python base
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1     PYTHONUNBUFFERED=1

WORKDIR /app

# System deps for psycopg2 and Pillow
RUN apt-get update && apt-get install -y --no-install-recommends     build-essential libpq-dev gcc curl netcat-traditional     && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# Create non-root user (optional)
RUN useradd -m appuser
USER appuser

EXPOSE 8000

# Entrypoint waits for DB then runs migrations and starts server
CMD ./entrypoint.sh
