# gunicorn_config.py

bind = "0.0.0.0:8004"
module = "core.wsgi:application"

workers = 1  # Adjust based on your server's resources
worker_connections = 1000
threads = 4

certfile = "/etc/letsencrypt/live/ekologiya.bahrombek.uz/fullchain.pem"
keyfile = "/etc/letsencrypt/live/ekologiya.bahrombek.uz/privkey.pem"