FROM python:3.9-alpine

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN mkdir requirements
ADD ./requirements/ /app/requirements
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements/production.txt


# copy project
COPY . .
