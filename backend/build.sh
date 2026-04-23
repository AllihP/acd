#!/usr/bin/env bash
set -o errexit

# 1. Build du Frontend
cd frontend
npm install
npm run build # Ici Vite crée le dossier 'dist'
cd ..

# 2. Préparation du Backend
cd backend
pip install -r requirements.txt

# 3. La fusion (Collectstatic)
# Django va prendre le 'index.html' de React et le mettre dans 'staticfiles'
python manage.py collectstatic --no-input --clear
python manage.py migrate