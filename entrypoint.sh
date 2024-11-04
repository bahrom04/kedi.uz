#!/bin/sh

python manage.py migrate
python manage.py tailwind install --no-input
python manage.py tailwind build --no-input
python manage.py collectstatic --no-input
python manage.py compilemessages

