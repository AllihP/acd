#!/usr/bin/env bash
# Arrêt immédiat en cas d'erreur
set -o errexit

# Définition du chemin de la racine du projet (un niveau au dessus de backend/)
ROOT_DIR=$(dirname "$(cd "$(dirname "$0")" && pwd)")

echo "🚀 Lancement du build complet ACD..."

# --- PARTIE FRONTEND ---
echo "📦 [1/4] Build du Frontend React..."
cd "$ROOT_DIR/frontend"
npm install
# Correction des permissions pour Vite
chmod +x node_modules/.bin/vite
npm run build

# --- PARTIE BACKEND ---
echo "🐍 [2/4] Installation des dépendances Python..."
cd "$ROOT_DIR/backend"
pip install --upgrade pip
pip install -r requirements.txt

echo "📂 [3/4] Collecte des fichiers statiques et migrations..."
# Rassemble React + Django Admin dans le dossier staticfiles
python manage.py collectstatic --no-input
python manage.py migrate

# --- SUPERUSER ---
echo "👤 [4/4] Vérification du compte administrateur..."
if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
  python manage.py createsuperuser \
    --no-input \
    --username "$DJANGO_SUPERUSER_USERNAME" \
    --email "$DJANGO_SUPERUSER_EMAIL" || true
fi

echo "✅ Build ACD terminé avec succès !"