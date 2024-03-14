upstream web_app {
    server backend:8004;
}

# Comment out the HTTPS section temporarily
# server {
#     listen 443 ssl;
#     server_name your_domain.com;

#     ssl_certificate /etc/letsencrypt/live/ekologiya.bahrombek.uz/fullchain.pem;
#     ssl_certificate_key /etc/letsencrypt/live/ekologiya.bahrombek.uz/privkey.pem;

#     access_log /var/log/nginx/access.log;
#     error_log /var/log/nginx/error.log;

#     location /static/ {
#         alias /var/www/static/;
#     }

#     location / {
#         proxy_pass http://web_app;
#         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
#         proxy_set_header Host $host;
#         proxy_redirect off;
#     }
# }

server {
    listen 80;
    server_name ekologiya.bahrombek.uz;

    location ~/.well-known/acme-challenge {
        allow all;
        root /var/www/certbot;
    }

    return 301 https://$host:$request_uri;
}