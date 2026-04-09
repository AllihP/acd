#!/usr/bin/env bash
set -o errexit

echo "──────────────────────────────────────"
echo " ACD — Build Script"
echo "──────────────────────────────────────"

pip install --upgrade pip
pip install -r requirements.txt

echo "→ Collecte des fichiers statiques..."
python manage.py collectstatic --no-input

echo "→ Application des migrations..."
python manage.py migrate

echo "→ Création du superutilisateur..."
python manage.py createsuperuser \
  --no-input \
  --username "$DJANGO_SUPERUSER_USERNAME" \
  --email    "$DJANGO_SUPERUSER_EMAIL" \
  2>/dev/null || echo "   Superuser déjà existant, ignoré."

echo "──────────────────────────────────────"
echo " Build terminé avec succès ✓"
echo "──────────────────────────────────────"