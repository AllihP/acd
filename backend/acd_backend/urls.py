from django.contrib import admin
from django.urls import path, include, re_path  # <-- 'path' doit être ici
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    # Accès admin sécurisé
    path('doulgue/', admin.site.urls), 
    
    # Endpoints API
    path('api/core/', include('apps.core.urls')),
    path('api/contact/', include('apps.contact.urls')),
    
    # Règle Catch-all pour le Frontend React
    # Cette ligne sert l'index.html pour toutes les routes non-API
    re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]

# Uniquement pour le développement local
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)