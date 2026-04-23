#!/usr/bin/env bash
set -o errexit

PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "🚀 [1/3] Construction du Frontend..."
cd "$PROJECT_ROOT/frontend"
npm install
chmod +x node_modules/.bin/vite
npm run build 

echo "🐍 [2/3] Installation du Backend..."
cd "$PROJECT_ROOT/backend"
pip install -r requirements.txt

echo "📂 [3/3] Collecte et Fix MIME Types..."
# Force la configuration pour éviter l'erreur 'Unknown command'
export DJANGO_SETTINGS_MODULE=acd_backend.settings
python -m django collectstatic --no-input --clear
python manage.py migrate

echo "✅ Déploiement ACD terminé !"