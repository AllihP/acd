#!/usr/bin/env bash
set -o errexit

echo "Building Frontend..."
cd frontend
npm install

# --- AJOUTER CETTE LIGNE POUR FIXER LES PERMISSIONS ---
chmod +x node_modules/.bin/vite

npm run build
cd ..

echo "Building Backend..."
cd backend
pip install -r requirements.txt

# Collecte des fichiers de React (dist) vers Django
python manage.py collectstatic --no-input
python manage.py migrate

# Création de l'admin secret (doulgue)
if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
  python manage.py createsuperuser \
    --no-input \
    --username "$DJANGO_SUPERUSER_USERNAME" \
    --email "$DJANGO_SUPERUSER_EMAIL" || true
fi