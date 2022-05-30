#!/bin/sh

python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input
# python manage.py runscript add_dumy_data
python manage.py runserver 0.0.0.0:8000