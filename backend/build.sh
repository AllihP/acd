#!/usr/bin/env bash
set -o errexit
set -o pipefail

# Render exécute les scripts depuis la racine du repo → pas besoin de calcul complexe
PROJECT_ROOT="$(pwd)"

echo "🚀 [1/3] Construction du Frontend..."
cd "$PROJECT_ROOT/frontend"

# Installation propre des dépendances
npm ci --prefer-offline --no-audit  # Plus rapide et fiable que npm install

# Build avec npx pour éviter les problèmes de permissions sur vite
npm run build

echo "🐍 [2/3] Installation du Backend..."
cd "$PROJECT_ROOT/backend"

# Installation des dépendances Python
pip install -r requirements.txt --no-cache-dir

echo "📂 [3/3] Collecte des statiques & Migrations..."
python manage.py collectstatic --no-input --clear
python manage.py migrate

echo "✅ Déploiement ACD terminé !"