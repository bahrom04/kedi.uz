FROM python:3.10.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


# set work directory
RUN mkdir code
WORKDIR /code


# Install gettext for internationalization
RUN apk add --no-cache gettext

# Copy requirements and install dependencies
COPY requirements/base.txt /code/base.txt
COPY requirements/production.txt /code/production.txt

RUN pip install pip --upgrade  && pip install -r production.txt


COPY . /code/


# Set executable permission for the entrypoint script

RUN ["chmod", "+x", "/code/docker-entrypoint.sh"]

# # Set the entrypoint
ENTRYPOINT ["sh","/code/docker-entrypoint.sh"]


