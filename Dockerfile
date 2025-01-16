FROM python:3.10.12-alpine

WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

# Install dependencies
RUN apk update && apk add --no-cache nodejs npm postgresql-dev gettext

# Create necessary directories
RUN mkdir -p /home/app/web/static /home/app/web/media /home/app/web/locale

# Set the app home directory
ENV APP_HOME=/home/app/web

WORKDIR $APP_HOME

# Copy project files into the container
COPY . .

# Install Python dependencies
RUN pip install pip --upgrade && pip install -r requirements/develop.txt

# Ensure entrypoint.sh is executable
RUN chmod +x /home/app/web/entrypoint.sh

# Set the entrypoint script
ENTRYPOINT ["sh", "/home/app/web/entrypoint.sh"]

# Clean up
RUN rm -rf /etc/apk/cache
