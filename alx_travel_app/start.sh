#!/usr/bin/env bash
# Exit on error
set -o errexit

# 1. Collect static files (Required for Swagger/Admin UI)
python manage.py collectstatic --no-input

# 2. Apply migrations
python manage.py migrate

# 3. Start Celery worker in the background (& is critical!)
celery -A alx_travel_app worker --loglevel=info --concurrency=1 &

# 4. Start the Gunicorn web server
gunicorn alx_travel_app.wsgi:application --bind 0.0.0.0:10000