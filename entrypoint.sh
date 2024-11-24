#!/usr/bin/sh

# Activate the virtual environment
activate_venv="$(pwd)/venv/bin/activate"
source $activate_venv

python manage.py migrate
python manage.py tailwind install --no-input
python manage.py tailwind build --no-input
python manage.py collectstatic --no-input
python manage.py compilemessages

# Restart services
sudo systemctl restart gunicorn
sudo systemctl restart nginx
echo "gunicorn and nginx restarted ..."