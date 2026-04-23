import os
from pathlib import Path
from decouple import config
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# --- APPLICATIONS ET MIDDLEWARE ---
# Assurez-vous que 'whitenoise.runserver_nostatic' est dans INSTALLED_APPS
# Assurez-vous que 'whitenoise.middleware.WhiteNoiseMiddleware' est juste après SecurityMiddleware

# --- CONFIGURATION DES FICHIERS STATIQUES ---
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Dossier du build de React
REACT_DIST_DIR = os.path.join(BASE_DIR.parent, 'frontend', 'dist')

STATICFILES_DIRS = [
    # On pointe vers la racine du build React
    REACT_DIST_DIR,
]

# CRITIQUE : Cette ligne permet à WhiteNoise de servir les fichiers avec le bon type MIME
# Elle crée un manifeste qui lie 'index-CbCKd3bS.css' au type 'text/css'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# On autorise WhiteNoise à servir les fichiers qui ne sont pas dans STATIC_ROOT (pour React)
WHITENOISE_INDEX_FILE = True

# --- TEMPLATES ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [REACT_DIST_DIR], # Django lit l'index.html directement depuis le build React
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]