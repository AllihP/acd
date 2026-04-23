#!/usr/bin/env bash
set -o errexit

PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "🚀 [1/3] Build Frontend..."
cd "$PROJECT_ROOT/frontend"
npm install
chmod +x node_modules/.bin/vite
npm run build 

echo "🐍 [2/3] Build Backend..."
cd "$PROJECT_ROOT/backend"
pip install -r requirements.txt

echo "📂 [3/3] Collecte des fichiers..."
# FORCE la configuration Django pour le collectstatic
export DJANGO_SETTINGS_MODULE=acd_backend.settings
python -m django collectstatic --no-input --clear
python manage.py migrate