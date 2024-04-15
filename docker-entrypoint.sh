#!/bin/bash


# Compile new translations
echo "Compile Messages"
python manage.py compilemessages --noinput

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput


# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting server"
gunicorn core.wsgi:application --bind 0.0.0.0:8000 --workers=4