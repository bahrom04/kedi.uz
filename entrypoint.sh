# !/usr/bin/sh

# Activate the virtual environment
activate_venv="$(pwd)/venv/bin/activate"
source $activate_venv

# python manage.py migrate
# python manage.py tailwind install --no-input
# python manage.py tailwind build --no-input
# python manage.py collectstatic --no-input
# python manage.py compilemessages

# # Restart services
# sudo systemctl restart gunicorn
# sudo systemctl restart nginx
# echo "gunicorn and nginx restarted ..."

if [ "$DB_USER" = "postgres" ]; then
    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done
fi

python manage.py migrate
python manage.py tailwind install --no-input
python manage.py tailwind build --no-input
python manage.py collectstatic --no-input
python manage.py compilemessages

exec "$@"