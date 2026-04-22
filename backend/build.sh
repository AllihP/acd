#!/usr/bin/env bash
# Arrêter le script en cas d'erreur
set -o errexit

# Installation des dépendances (via Pip ou Poetry)
# Si vous utilisez Poetry, remplacez par : poetry install
pip install -r requirements.txt

# Préparation de la base de données
python manage.py migrate

# Collecte des fichiers statiques pour la production
python manage.py collectstatic --no-input