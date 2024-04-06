FROM python:3.10.12

RUN apt-get update && \
    apt-get install -y gettext
    
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir code
WORKDIR /code
COPY requirements/ /code/
RUN pip install --upgrade pip
RUN pip install -r production.txt
COPY . /code/
