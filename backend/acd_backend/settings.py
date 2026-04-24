import os
from pathlib import Path
from decouple import config
import dj_database_url

# =============================================================================
# CHEMINS DE BASE
# =============================================================================
# Chemins de base
BASE_DIR = Path(__file__).resolve().parent.parent

# =============================================================================
# SÉCURITÉ
# =============================================================================
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS', 
    default='acd-fqjq.onrender.com,localhost,127.0.0.1'
).split(',')

# =============================================================================
# APPLICATIONS
# =============================================================================
INSTALLED_APPS = [
    # Interface admin moderne (doit être en premier)
    'unfold',
    # Django contrib
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    # Apps tierces
    'rest_framework',
    'corsheaders',
    # Apps locales
    'apps.core',
    'apps.contact',
]

# =============================================================================
# MIDDLEWARE (Ordre critique)
# =============================================================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Juste après SecurityMiddleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',       # Avant CommonMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'acd_backend.urls'
WSGI_APPLICATION = 'acd_backend.wsgi.application'  # ← Requis par Gunicorn

# =============================================================================
# TEMPLATES (Point d'entrée React/Vite)
# =============================================================================
REACT_DIST_DIR = BASE_DIR.parent / 'frontend' / 'dist'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [REACT_DIST_DIR],  # Django sert l'index.html de Vite
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

# =============================================================================
# BASE DE DONNÉES (Neon PostgreSQL + PgBouncer)
# =============================================================================
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL'),
        conn_max_age=0,              # ← 0 OBLIGATOIRE si DATABASE_URL contient ?pgbouncer=true
        ssl_require=True,            # ← Neon exige SSL
        conn_health_checks=True,     # ← Détection des connexions mortes (Render)
    )
}

# =============================================================================
# FICHIERS STATIQUES ET MÉDIAS (Django 4.2+ compatible)
# =============================================================================
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [REACT_DIST_DIR]  # Dossier de sortie du build Vite

# ✅ Configuration WhiteNoise compatible Django 4.2+ (remplace STATICFILES_STORAGE)
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# =============================================================================
# CONFIGURATION CORS
# =============================================================================
CORS_ALLOWED_ORIGINS = [
    "https://acd-fqjq.onrender.com",
    "http://localhost:5173",  # Vite dev server
]
CORS_ALLOW_CREDENTIALS = True

# =============================================================================
# PARAMÈTRES PAR DÉFAUT
# =============================================================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'