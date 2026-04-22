import os
from pathlib import Path
from decouple import config
import dj_database_url
from django.urls import reverse_lazy

# ── CHEMINS DE BASE ───────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent

# ── SÉCURITÉ ──────────────────────────────────────────────────────────
# En production sur Render, la SECRET_KEY est générée automatiquement
SECRET_KEY = config('SECRET_KEY', default='django-insecure-fallback-key-for-dev')

# DEBUG doit être False en production
DEBUG = config('DEBUG', default=False, cast=bool)

# Autorise l'URL de votre backend Render et le localhost pour le dev
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1').split(',')

# ── APPLICATIONS ──────────────────────────────────────────────────────
INSTALLED_APPS = [
    'unfold',  # Doit être avant django.contrib.admin
    'unfold.contrib.filters',
    'unfold.contrib.forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic', # Pour les fichiers statiques
    'django.contrib.staticfiles',
    
    # Librairies tierces
    'rest_framework',
    'corsheaders',
    'django_filters',
    'drf_spectacular',
    
    # Vos applications locales
    'apps.core',
    'apps.contact',
]

# ── MIDDLEWARE ────────────────────────────────────────────────────────
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Indispensable pour Render
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'acd_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# ── BASE DE DONNÉES ───────────────────────────────────────────────────
# Utilise DATABASE_URL (PostgreSQL) sur Render, sinon SQLite en local
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600
    )
}

# ── VALIDATION DES MOTS DE PASSE ──────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ── INTERNATIONALISATION ──────────────────────────────────────────────
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Africa/Ndjamena'
USE_I18N = True
USE_TZ = True

# ── FICHIERS STATIQUES ET MÉDIAS ──────────────────────────────────────
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Optimisation WhiteNoise pour la production
if not DEBUG:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ── CONFIGURATION CORS ────────────────────────────────────────────────
CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS', default='http://localhost:5173').split(',')
CORS_ALLOW_CREDENTIALS = True

# ── PARAMÈTRES DE SÉCURITÉ PRODUCTION ─────────────────────────────────
if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

# ── CONFIGURATION UNFOLD ADMIN ────────────────────────────────────────
UNFOLD = {
    "SITE_TITLE": "ACD Admin",
    "SITE_HEADER": "Administration ACD",
    "SITE_SYMBOL": "speed",
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": False,
        "navigation": [
            {
                "title": "Contenu",
                "separator": True,
                "items": [
                    {
                        "title": "Portfolio",
                        "icon": "photo_library",
                        "link": reverse_lazy("admin:core_portfolioitem_changelist"),
                    },
                    {
                        "title": "Témoignages",
                        "icon": "format_quote",
                        "link": reverse_lazy("admin:core_testimonial_changelist"),
                    },
                ],
            },
            {
                "title": "Contact",
                "items": [
                    {
                        "title": "Messages",
                        "icon": "mail",
                        "link": reverse_lazy("admin:contact_contactmessage_changelist"),
                    },
                ],
            },
        ],
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'