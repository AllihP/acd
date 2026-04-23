#!/usr/bin/env bash
set -o errexit

# Définition de la racine
ROOT_DIR=$(dirname "$(cd "$(dirname "$0")" && pwd)")

echo "🚀 Étape 1 : Build du Frontend (Vite)..."
cd "$ROOT_DIR/frontend"
npm install
chmod +x node_modules/.bin/vite
npm run build # Génère le dossier dist/

echo "🐍 Étape 2 : Préparation du Backend (Django)..."
cd "$ROOT_DIR/backend"
pip install -r requirements.txt

# IMPORTANT : On vide l'ancien dossier pour éviter les erreurs MIME
echo "📂 Étape 3 : Collecte des fichiers statiques..."
python manage.py collectstatic --no-input --clear
python manage.py migrate

echo "✅ Déploiement ACD réussi !"