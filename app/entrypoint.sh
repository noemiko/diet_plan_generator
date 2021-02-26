#!/bin/sh


echo "Waiting for postgres..."
#while ! nc -z $SQL_HOST $SQL_PORT; do
#  sleep 5.1
#done
echo "Waiting for postgres..."

while ! nc -z db 5432; do
  sleep 0.1
done
echo "PostgreSQL started"

python manage.py migrate

exec "$@"
