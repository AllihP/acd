from django.contrib import admin
from django.urls import path, include, re_path  # <-- 'path' doit être présent ici
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    # Accès à l'administration Unfold
    path('doulgue/', admin.site.urls), 
    
    # Endpoints de l'API ACD
    path('api/core/', include('apps.core.urls')),
    path('api/contact/', include('apps.contact.urls')),
    
    # Règle pour servir le Frontend React
    # Sert l'index.html pour toutes les routes qui ne sont pas des API
    re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]

# Service des fichiers médias en mode développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)