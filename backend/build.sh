#!/usr/bin/env bash
set -o errexit

# 1. Build du Frontend
cd frontend
npm install
chmod +x node_modules/.bin/vite
npm run build 
cd ..

# 2. Préparation Django
cd backend
pip install -r requirements.txt
# Le flag --clear supprime les vieux fichiers index.html erronés
python manage.py collectstatic --no-input --clear
python manage.py migrate