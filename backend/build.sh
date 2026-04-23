#!/usr/bin/env bash
set -o errexit

# Se placer à la racine du projet (Render exécute les scripts depuis la racine du repo)
PROJECT_ROOT="$(pwd)"

echo "🚀 [1/3] Construction du Frontend..."
cd "$PROJECT_ROOT/frontend"
npm install
npm run build

echo "🐍 [2/3] Installation du Backend..."
cd "$PROJECT_ROOT/backend"
pip install -r requirements.txt --no-cache-dir

echo "📂 [3/3] Collecte des fichiers statiques & Migrations..."
# DJANGO_SETTINGS_MODULE est automatiquement chargé via manage.py
python manage.py collectstatic --no-input --clear
python manage.py migrate

echo "✅ Déploiement ACD terminé !"