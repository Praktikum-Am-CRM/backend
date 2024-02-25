#!/bin/bash

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  echo 'Waiting for postgres to start...'
  sleep 3
done
echo 'Postgres started'

python manage.py migrate
python manage.py collectstatic --no-input

gunicorn backend.wsgi:application --bind 0:8000
