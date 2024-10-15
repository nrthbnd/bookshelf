#!/bin/sh

# Переходим в папку app
cd /fastapi_app/app

echo "Applying database migrations..."
alembic upgrade head

if [ $? -ne 0 ]; then
    echo "Failed to apply migrations"
    exit 1
fi

echo "Starting Uvicorn server..."
uvicorn main:app --host=0.0.0.0 --port=8000
