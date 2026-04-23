#!/usr/bin/env bash
set -o errexit

# Chemins
ROOT_DIR=$(dirname "$(cd "$(dirname "$0")" && pwd)")

echo "🚀 Nettoyage et Build..."
cd "$ROOT_DIR/frontend"
npm install
chmod +x node_modules/.bin/vite
npm run build

echo "🐍 Préparation Django..."
cd "$ROOT_DIR/backend"
pip install -r requirements.txt

# IMPORTANT: On s'assure que le dossier staticfiles est propre
python manage.py collectstatic --no-input --clear 
python manage.py migrate