#!/usr/bin/sh

# Activate the virtual environment
source ./venv/bin/activate

python manage.py migrate
python manage.py tailwind install --no-input
python manage.py tailwind build --no-input
python manage.py collectstatic --no-input
python manage.py compilemessages

# Restart services
sudo systemctl restart gunicorn
sudo systemctl restart nginx