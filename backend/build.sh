#!/usr/bin/env bash
set -o errexit

ROOT_DIR=$(dirname "$(cd "$(dirname "$0")" && pwd)")

echo "🚀 [1/3] Construction du Frontend..."
cd "$ROOT_DIR/frontend"
npm install
chmod +x node_modules/.bin/vite
npm run build 

echo "🐍 [2/3] Préparation du Backend..."
cd "$ROOT_DIR/backend"
pip install -r requirements.txt

echo "📂 [3/3] Nettoyage et Collecte des Statiques..."
# Le flag --clear est INDISPENSABLE pour supprimer les vieux fichiers MIME corrompus
python manage.py collectstatic --no-input --clear
python manage.py migrate

echo "✅ Build ACD réussi !"