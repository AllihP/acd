from pathlib import Path
from decouple import config
from django.urls import reverse_lazy
from django.templatetags.static import static

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY', default='django-insecure-acd-dev-key-changeme-in-production')
DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1').split(',')

INSTALLED_APPS = [
    'unfold',
    'unfold.contrib.filters',
    'unfold.contrib.forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'django_filters',
    'apps.core',
    'apps.contact',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Africa/Ndjamena'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ── CORS ───────────────────────────────────────────────────────────────
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:3000",
]
CORS_ALLOW_ALL_ORIGINS = config('CORS_ALLOW_ALL', default=False, cast=bool)

# ── DRF ────────────────────────────────────────────────────────────────
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
}

# ── UNFOLD — Design Admin Personnalisé ACD ────────────────────────────
UNFOLD = {
    "SITE_TITLE": "ACD Admin",
    "SITE_HEADER": "ACD",
    "SITE_SUBHEADER": "Agence de Communication pour le Développement",
    "SITE_URL": "http://localhost:5173",
    "SITE_ICON": None,
    "SITE_LOGO": None,
    "SITE_SYMBOL": "settings",
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "STYLES": [
        lambda request: static("admin/css/custom_admin.css"),
    ],
    "SCRIPTS": [],
    # Palette couleurs ACD : Navy #0C1931 · Blue #3A5F8A
    "COLORS": {
        "primary": {
            "50":  "240 244 248",
            "100": "220 229 238",
            "200": "183 203 221",
            "300": "130 163 194",
            "400": "84 127 168",
            "500": "58 95 138",    # --acd-blue
            "600": "46 76 111",
            "700": "36 60 87",
            "800": "25 43 66",
            "900": "12 25 49",     # --acd-navy
            "950": "6 13 26",
        },
    },
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": False,
        "navigation": [
            {
                "title": "Contenu du site",
                "separator": True,
                "collapsible": False,
                "items": [
                    {
                        "title": "Paramètres",
                        "icon": "settings",
                        "link": reverse_lazy("admin:core_sitesettings_changelist"),
                    },
                    {
                        "title": "Hero",
                        "icon": "home",
                        "link": reverse_lazy("admin:core_herosection_changelist"),
                    },
                    {
                        "title": "À propos",
                        "icon": "business",
                        "link": reverse_lazy("admin:core_aboutsection_changelist"),
                    },
                    {
                        "title": "Services",
                        "icon": "star",
                        "link": reverse_lazy("admin:core_service_changelist"),
                    },
                    {
                        "title": "Pourquoi nous",
                        "icon": "check_circle",
                        "link": reverse_lazy("admin:core_whyitem_changelist"),
                    },
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
                "separator": True,
                "collapsible": False,
                "items": [
                    {
                        "title": "Messages",
                        "icon": "mail",
                        "link": reverse_lazy("admin:contact_contactmessage_changelist"),
                    },
                ],
            },
            {
                "title": "Administration",
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": "Utilisateurs",
                        "icon": "person",
                        "link": reverse_lazy("admin:auth_user_changelist"),
                    },
                    {
                        "title": "Groupes",
                        "icon": "group",
                        "link": reverse_lazy("admin:auth_group_changelist"),
                    },
                ],
            },
        ],
    },
}
