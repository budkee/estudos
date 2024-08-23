#!/bin/bash

# --------------- Django Backend Setup -----------------
# ./wait-for-it.sh db:7777

## Criação das tabelas no PostgreSQL
./manage.py migrate
./manage.py migrate --database=db_data data
./manage.py migrate --database=db_newsletter newsletter


# --------------- Django Start Server w/ API Gateway -----------------
# ./manage.py collectstatic --no-input  # This will copy all files from your static folders into the STATIC_ROOT directory.
# gunicorn api.wsgi:application --bind 0.0.0.0:8000 -> Verificar por que os arquivos dinâmicos não estãoo sendo entregues

# --------------- Django Start Server -----------------
./manage.py runserver 0.0.0.0:8000
