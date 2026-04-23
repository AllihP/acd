from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
import os

urlpatterns = [
    # Admin secret
    path('doulgue/', admin.site.urls),
    
    # API Endpoints
    path('api/core/', include('apps.core.urls')),
    path('api/contact/', include('apps.contact.urls')),

    # Servir les fichiers statiques (assets) explicitement
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    
    # Catch-all pour React : Sert l'index.html PHYSIQUE généré dans staticfiles
    re_path(r'^.*$', serve, {
        'document_root': settings.STATIC_ROOT,
        'path': 'index.html'
    }),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)