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
    'unfold',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'apps.core',
    'apps.contact',
]

# =============================================================================
# MIDDLEWARE
# =============================================================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'acd_backend.urls'
WSGI_APPLICATION = 'acd_backend.wsgi.application'

# =============================================================================
# TEMPLATES
# =============================================================================
REACT_DIST_DIR = BASE_DIR.parent / 'frontend' / 'dist'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [REACT_DIST_DIR],
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
# BASE DE DONNÉES (Neon + PgBouncer)
# =============================================================================
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL'),
        conn_max_age=0,  # ← 0 si DATABASE_URL contient ?pgbouncer=true
        ssl_require=True
    )
}

# =============================================================================
# STATIQUES ET MÉDIAS (CORRIGÉ : STORAGES compatible Django 6.0.3)
# =============================================================================
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [REACT_DIST_DIR]

# ✅ Remplace STATICFILES_STORAGE (déprécié Django 4.2+)
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
# CORS
# =============================================================================
CORS_ALLOWED_ORIGINS = [
    "https://acd-fqjq.onrender.com",
    "http://localhost:5173",
]
CORS_ALLOW_CREDENTIALS = True

# =============================================================================
# PARAMÈTRES PAR DÉFAUT
# =============================================================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'