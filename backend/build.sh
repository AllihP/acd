#!/usr/bin/env bash
# Exit on error
set -o errexit

echo "🚀 Lancement du build complet ACD..."

# --- PARTIE FRONTEND ---
echo "📦 [1/4] Build du Frontend React..."
cd ../frontend
npm install
# Correction impérative des droits pour Vite sur Render
chmod +x node_modules/.bin/vite
npm run build
cd ../backend

# --- PARTIE BACKEND ---
echo "🐍 [2/4] Installation des dépendances Python..."
pip install --upgrade pip
pip install -r requirements.txt

echo "📂 [3/4] Collecte des fichiers statiques et migrations..."
# Cette commande va copier les fichiers du dossier frontend/dist vers backend/staticfiles
python manage.py collectstatic --no-input
python manage.py migrate

# --- OPTIONNEL : SUPERUSER ---
echo "👤 [4/4] Vérification du compte administrateur..."
if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
  python manage.py createsuperuser \
    --no-input \
    --username "$DJANGO_SUPERUSER_USERNAME" \
    --email "$DJANGO_SUPERUSER_EMAIL" || true
fi

echo "✅ Build ACD terminé avec succès !"