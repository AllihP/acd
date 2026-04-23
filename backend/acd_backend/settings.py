import os
from pathlib import Path
from decouple import config
import dj_database_url

# 1. Chemins de base
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Sécurité
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='acd-fqjq.onrender.com,localhost,127.0.0.1').split(',')

# 3. Applications
INSTALLED_APPS = [
    'unfold', # Interface moderne pour l'administration
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic', # Optimisation des fichiers statiques
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'apps.core',
    'apps.contact',
]

# 4. Middleware (L'ordre est CRITIQUE pour éviter les erreurs MIME)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Doit être juste après SecurityMiddleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'acd_backend.urls'

# 5. Templates (Configuré pour lire l'index.html de React)
REACT_DIST_DIR = BASE_DIR.parent / 'frontend' / 'dist'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [REACT_DIST_DIR], # Django va chercher l'index.html directement ici
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

# 6. Base de données (Neon)
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL'),
        conn_max_age=600
    )
}

# 7. Gestion des fichiers Statiques (Le cœur du problème MIME)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Dossiers où Django cherche les fichiers avant collectstatic
STATICFILES_DIRS = [
    REACT_DIST_DIR, # Contient le dossier /assets généré par Vite
]

# Utilisation de WhiteNoise pour servir et compresser les fichiers (évite les erreurs MIME)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# 8. Médias (Images du Portfolio)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 9. CORS & Sécurité supplémentaire
CORS_ALLOWED_ORIGINS = [
    "https://acd-fqjq.onrender.com",
    "http://localhost:5173",
]
CORS_ALLOW_CREDENTIALS = True

# Sécurité HTTPS pour la production Render
if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'