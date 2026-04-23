#!/usr/bin/env bash
set -o errexit

# On monte d'un niveau pour aller dans le frontend
cd ..
cd frontend
npm install
chmod +x node_modules/.bin/vite
npm run build # Génère le dossier 'dist'

# On revient dans le dossier backend
cd ../backend

# On crée manuellement le dossier de destination pour éviter tout bug
mkdir -p staticfiles

# SOLUTION RADICALE : On copie physiquement les fichiers de React dans Django
echo "🚚 Transfert direct des fichiers React..."
cp -r ../frontend/dist/* ./staticfiles/

# Installation des dépendances Python
pip install -r requirements.txt

# On lance les migrations (sans collectstatic car on a déjà copié les fichiers)
python manage.py migrate