#!/usr/bin/env bash
set -o errexit
set -o pipefail

PROJECT_ROOT="$(pwd)"

echo "🚀 [1/3] Construction du Frontend..."
cd "$PROJECT_ROOT/frontend"
npm ci --prefer-offline --no-audit
npm run build

echo "🐍 [2/3] Installation du Backend..."
cd "$PROJECT_ROOT/backend"
pip install -r requirements.txt --no-cache-dir

echo "📂 [3/3] Collecte des statiques & Migrations..."
export DJANGO_SETTINGS_MODULE=acd_backend.settings
python manage.py collectstatic --no-input --clear
python manage.py migrate

echo "✅ Déploiement ACD terminé !"