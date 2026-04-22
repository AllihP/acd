import os
from pathlib import Path
from decouple import config
import dj_database_url
from django.urls import reverse_lazy

# --- CHEMINS DE BASE ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- SÉCURITÉ ---
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

# On autorise votre domaine Render et le local
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='acd-fqjq.onrender.com,localhost,127.0.0.1').split(',')

# --- APPLICATIONS ---
INSTALLED_APPS = [
    'unfold',  # Avant admin
    'unfold.contrib.filters',
    'unfold.contrib.forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    
    # Tierces
    'rest_framework',
    'corsheaders',
    'django_filters',
    'drf_spectacular',
    
    # Local
    'apps.core',
    'apps.contact',
]

# --- MIDDLEWARE ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Gestion optimisée des statiques
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
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# --- BASE DE DONNÉES (Configuration Neon/PostgreSQL) ---
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL'),
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# --- VALIDATION DES MOTS DE PASSE ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --- INTERNATIONALISATION ---
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Africa/Ndjamena'
USE_I18N = True
USE_TZ = True

# --- FICHIERS STATIQUES ET MÉDIAS ---
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_DIRS = [
    BASE_DIR / "staticfiles", 
]

MEDIA_URL = 'https://acd-fqjq.onrender.com/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# --- CONFIGURATION CORS (Sécurité pour le Frontend) ---
CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS', default='https://acd-frontend.onrender.com').split(',')
CORS_ALLOW_CREDENTIALS = True

# --- REST FRAMEWORK ---
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# --- SÉCURITÉ PRODUCTION ---
if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

# --- CONFIGURATION UNFOLD ADMIN ---
UNFOLD = {
    "SITE_TITLE": "ACD Admin",
    "SITE_HEADER": "Administration ACD",
    "SHOW_HISTORY": True,
    "SIDEBAR": {
        "show_search": True,
        "navigation": [
            {
                "title": "Contenu",
                "items": [
                    {"title": "Portfolio", "icon": "photo_library", "link": reverse_lazy("admin:core_portfolioitem_changelist")},
                    {"title": "Témoignages", "icon": "format_quote", "link": reverse_lazy("admin:core_testimonial_changelist")},
                ],
            },
            {
                "title": "Contact",
                "items": [
                    {"title": "Messages", "icon": "mail", "link": reverse_lazy("admin:contact_contactmessage_changelist")},
                ],
            },
        ],
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'