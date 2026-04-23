#!/usr/bin/env bash
set -o errexit
set -o pipefail

# Render exécute toujours depuis la racine du repo
PROJECT_ROOT="$(pwd)"

echo "🚀 [1/3] Construction du Frontend (Vite)..."
cd "$PROJECT_ROOT/frontend"
npm ci --prefer-offline --no-audit
npm run build  # → Génère frontend/dist avec index.html et assets/

echo "🐍 [2/3] Installation du Backend (Django)..."
cd "$PROJECT_ROOT/backend"
pip install -r requirements.txt --no-cache-dir

echo "📂 [3/3] Collecte des statiques & Migrations..."
# manage.py charge automatiquement acd_backend.settings
python manage.py collectstatic --no-input --clear
python manage.py migrate --no-input

echo "✅ Déploiement ACD terminé !"