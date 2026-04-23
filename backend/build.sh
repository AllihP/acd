#!/usr/bin/env bash
set -o errexit

# Définition de la racine
ROOT_DIR=$(dirname "$(cd "$(dirname "$0")" && pwd)")

echo "🚀 [1/3] Build du Frontend..."
cd "$ROOT_DIR/frontend"
npm install
# FORCER LA PERMISSION ICI
chmod +x node_modules/.bin/vite
npm run build 

echo "🐍 [2/3] Installation Django..."
cd "$ROOT_DIR/backend"
pip install -r requirements.txt

echo "📂 [3/3] Collecte et Nettoyage des Statiques..."
# Le flag --clear est vital pour supprimer les vieux fichiers index.html erronés
python manage.py collectstatic --no-input --clear
python manage.py migrate

echo "✅ Build ACD réussi !"