#!/usr/bin/env bash
set -o errexit

# 1. Build Frontend
cd frontend
npm install
chmod +x node_modules/.bin/vite
npm run build # Génère le dossier dist/
cd ..

# 2. Build Backend
cd backend
pip install -r requirements.txt

# 3. Collectstatic (C'est ici que Django lie tout)
# Le flag --clear est vital pour éviter les vieux fichiers MIME erronés
python manage.py collectstatic --no-input --clear
python manage.py migrate