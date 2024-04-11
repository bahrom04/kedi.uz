FROM python:3.10.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


# set work directory
WORKDIR /usr/src/app


# Install PostgreSQL client library
RUN apk update && \
    apk add --no-cache postgresql-dev

# Install gettext for internationalization
RUN apk add --no-cache gettext

# Copy requirements and install dependencies
COPY requirements/base.txt base.txt
COPY requirements/production.txt production.txt

RUN pip install pip --upgrade  && pip install -r production.txt


RUN mkdir -p /home/app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
RUN mkdir $APP_HOME/media

WORKDIR $APP_HOME

COPY . .


# Set executable permission for the entrypoint script

RUN ["chmod", "+x", "/home/app/web/docker-entrypoint.sh"]

# # Set the entrypoint
ENTRYPOINT ["sh","/home/app/web/docker-entrypoint.sh"]

# Remove the package manager cache
RUN rm -rf /etc/apk/cache
