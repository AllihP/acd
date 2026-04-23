import os
from pathlib import Path
from decouple import config
import dj_database_url

# Chemins de base
BASE_DIR = Path(__file__).resolve().parent.parent

# --- SÉCURITÉ ---
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
# On s'assure que le domaine Render est autorisé
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='acd-fqjq.onrender.com,localhost,127.0.0.1').split(',')

# --- APPLICATIONS ---
INSTALLED_APPS = [
    'unfold', # Interface moderne
    'unfold.contrib.filters',
    'unfold.contrib.forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic', # Optimisation statique
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'apps.core',
    'apps.contact',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Indispensable pour servir React
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'acd_backend.urls'

# --- TEMPLATES ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Django doit chercher l'index.html dans le dossier où collectstatic rassemble tout
        'DIRS': [os.path.join(BASE_DIR, 'staticfiles')], 
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

WSGI_APPLICATION = 'acd_backend.wsgi.application'

# --- BASE DE DONNÉES (Neon/PostgreSQL) ---
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL'),
        conn_max_age=600
    )
}

# --- FICHIERS STATIQUES (FIX MIME TYPE & VITE) ---
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Dossier source de React (Vite build)
REACT_DIST_DIR = os.path.join(BASE_DIR.parent, 'frontend', 'dist')

STATICFILES_DIRS = [
    os.path.join(REACT_DIST_DIR, 'assets'), 
    REACT_DIST_DIR,
]
# Gestion du cache et de la compression pour éviter les erreurs MIME
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Médias (Images du Portfolio)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# --- CONFIGURATION SUPPLÉMENTAIRE ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuration CORS pour autoriser le frontend
CORS_ALLOWED_ORIGINS = [
    "https://acd-fqjq.onrender.com",
    "http://localhost:5173",
]

# --- PARAMÈTRES UNFOLD (ACD ADMIN) ---
UNFOLD = {
    "SITE_TITLE": "ACD Admin",
    "SITE_HEADER": "Agence de Communication pour le Développement",
    "SITE_SYMBOL": "speed", # Icône dashboard
    "COLORS": {
        "primary": {
            "50": "250 245 255",
            "100": "243 232 255",
            "500": "168 85 247",
            "600": "147 51 234",
            "900": "88 28 135",
        },
    },
}