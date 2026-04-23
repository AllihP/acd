import os
from pathlib import Path
from decouple import config
import dj_database_url

# =============================================================================
# CHEMINS DE BASE
# =============================================================================
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
# APPLICATIONS (Ordre critique pour Unfold)
# =============================================================================
INSTALLED_APPS = [
    'unfold',  # Interface admin moderne
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',  # Service statique optimisé
    'django.contrib.staticfiles',
    
    # Apps tierces
    'rest_framework',
    'corsheaders',
    'drf_spectacular',  # Documentation API OpenAPI
    'django_filters',   # Filtrage API
    
    # Apps locales
    'apps.core',
    'apps.contact',
]

# =============================================================================
# MIDDLEWARE
# =============================================================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Doit être juste après SecurityMiddleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',       # Doit être avant CommonMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'acd_backend.urls'
WSGI_APPLICATION = 'acd_backend.wsgi.application'

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
# BASE DE DONNÉES (Neon PostgreSQL)
# =============================================================================
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True
    )
}

# =============================================================================
# FICHIERS STATIQUES ET MÉDIAS
# =============================================================================
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    REACT_DIST_DIR,  # Contient le dossier /assets de Vite
]

# Configuration WhiteNoise compatible Django 4.2+
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
# DJANGO REST FRAMEWORK
# =============================================================================
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
}

# =============================================================================
# DRF SPECTACULAR - Documentation API
# =============================================================================
SPECTACULAR_SETTINGS = {
    'TITLE': 'ACD API',
    'DESCRIPTION': 'API documentation for ACD project',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'COMPONENT_SPLIT_REQUEST': True,
}

# =============================================================================
# DJANGO UNFOLD - Admin moderne
# =============================================================================
UNFOLD = {
    "SITE_TITLE": "ACD Admin",
    "SITE_HEADER": "ACD Administration",
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": False,
}

# =============================================================================
# INTERNATIONALISATION
# =============================================================================
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# =============================================================================
# PARAMÈTRES PAR DÉFAUT
# =============================================================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# =============================================================================
# LOGGING (Production-safe)
# =============================================================================
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}