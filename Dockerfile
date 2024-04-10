FROM python:3.10.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

# Install PostgreSQL client library
RUN apk update && \
    apk add --no-cache postgresql-dev

# Install gettext for internationalization
RUN apk add --no-cache gettext

# Copy requirements and install dependencies
COPY requirements/ /code/
RUN pip install --upgrade pip && \
    pip install -r production.txt

# Copy the application code
COPY . /code/

# Set executable permission for the entrypoint script

RUN ["chmod", "+x", "/code/docker-entrypoint.sh"]

# # Set the entrypoint
ENTRYPOINT ["sh","/code/docker-entrypoint.sh"]
