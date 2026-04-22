#!/usr/bin/env bash
set -o errexit

# Installation
pip install -r requirements.txt

# Migrations vers Neon
python manage.py migrate
python manage.py collectstatic --no-input

# Création sécurisée de l'admin
if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
  python manage.py createsuperuser \
    --no-input \
    --username "$DJANGO_SUPERUSER_USERNAME" \
    --email "$DJANGO_SUPERUSER_EMAIL" || true
fi