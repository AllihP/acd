#!/usr/bin/env bash
# Arrêter le script en cas d'erreur
set -o errexit

# --- 1. BUILD FRONTEND ---
echo "Building Frontend..."
cd frontend
npm install
npm run build
cd ..

# --- 2. PREPARATION BACKEND ---
echo "Building Backend..."
cd backend
pip install -r requirements.txt

# On déplace les fichiers compilés de React vers un dossier que Django peut voir
mkdir -p staticfiles
cp -r ../frontend/dist/* ./staticfiles/

# Migrations et Statiques
python manage.py migrate
python manage.py collectstatic --no-input

# Création de l'admin (URL secrète déjà configurée dans vos logs)
if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
  python manage.py createsuperuser \
    --no-input \
    --username "$DJANGO_SUPERUSER_USERNAME" \
    --email "$DJANGO_SUPERUSER_EMAIL" || true
fi