#!/usr/bin/env bash
set -o errexit
set -o pipefail

# Render exécute depuis la racine du repo → pwd suffit
PROJECT_ROOT="$(pwd)"

echo "🚀 [1/3] Construction du Frontend (Vite)..."
cd "$PROJECT_ROOT/frontend"
npm ci --prefer-offline --no-audit
npm run build  # → génère frontend/dist avec base: '/static/'

echo "🐍 [2/3] Installation du Backend (Django)..."
cd "$PROJECT_ROOT/backend"
pip install -r requirements.txt --no-cache-dir

echo "📂 [3/3] Collecte des statiques & Migrations..."
# manage.py charge automatiquement DJANGO_SETTINGS_MODULE
python manage.py collectstatic --no-input --clear
python manage.py migrate --no-input

echo "✅ Déploiement ACD terminé !"