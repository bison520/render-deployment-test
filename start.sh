#!/bin/bash
# Start script for Render deployment

# Get the port from environment variable
PORT="${PORT:-10000}"

# Start the application with gunicorn
exec gunicorn --bind 0.0.0.0:$PORT --workers 2 --timeout 30 app:app
