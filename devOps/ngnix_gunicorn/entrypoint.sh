#!/bin/bash

# Realiza as criações no BD
python manage.py migrate
python manage.py collectstatic

gunicorn api.wsgi:application --bind 0.0.0.0:8000