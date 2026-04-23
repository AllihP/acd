#!/usr/bin/env bash
set -o errexit

# On définit proprement la racine du projet (un niveau au-dessus de ce script)
PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "🚀 [1/3] Construction du Frontend React..."
cd "$PROJECT_ROOT/frontend"
npm install
chmod +x node_modules/.bin/vite
npm run build 

echo "🐍 [2/3] Installation du Backend Django..."
cd "$PROJECT_ROOT/backend"
# Création du dossier statique pour éviter toute erreur système
mkdir -p staticfiles
pip install -r requirements.txt

echo "📂 [3/3] Fusion et Collecte des fichiers..."
# On force l'utilisation du module Django installé pour éviter 'Unknown command'
python -m django collectstatic --no-input --clear
python manage.py migrate

echo "✅ Build ACD terminé avec succès !"