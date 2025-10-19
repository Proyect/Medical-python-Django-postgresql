# syntax=docker/dockerfile:1.7-labs

FROM python:3.12-slim AS base
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

# System deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
  && rm -rf /var/lib/apt/lists/*

# Install Python deps
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY crud ./crud

# Create a non-root user and ensure ownership of app dir
RUN useradd --create-home appuser && chown -R appuser:appuser /app
USER appuser

# Collect static at build time (optional; harmless if none)
ENV DJANGO_DEBUG=false
RUN python crud/manage.py collectstatic --noinput || true

# Expose port
EXPOSE 8000

# Entrypoint command using gunicorn
ENV DJANGO_SETTINGS_MODULE=crud.crud.settings
CMD ["gunicorn", "crud.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "120"]
