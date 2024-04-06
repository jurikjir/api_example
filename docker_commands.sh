#!/bin/bash

CPU_CORES=$(nproc --all)
WORKERS_NUM=$((CPU_CORES + 1))
HOST=0.0.0.0
PORT=8000

pytest --verbose --pyargs src
echo "Starting the API service with '$WORKERS_NUM' workers..."
uvicorn src.app_custom_validations:app --workers $WORKERS_NUM --host $HOST --port $PORT