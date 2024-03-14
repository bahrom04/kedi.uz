FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir code
WORKDIR /code
COPY requirements/ /code/
RUN pip install --upgrade pip
RUN pip install -r base.txt
COPY . /code/
