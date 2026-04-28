#!/usr/bin/env bash
set -o errexit
set -o pipefail

echo "🐍 [1/2] Installation du Backend (Django)..."
pip install -r requirements.txt --no-cache-dir

echo "📂 [2/2] Collecte des statiques & Migrations..."
# manage.py charge automatiquement acd_backend.settings
python manage.py collectstatic --no-input --clear
python manage.py migrate --no-input

echo "✅ Déploiement du backend terminé !"