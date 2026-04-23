from django.contrib import admin  # <-- CET IMPORT MANQUAIT
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    # Votre accès secret pour l'admin
    path('doulgue/', admin.site.urls), 
    
    # Points d'accès de l'API
    path('api/core/', include('apps.core.urls')),
    path('api/contact/', include('apps.contact.urls')),
    
    # Sert l'index de React pour toutes les autres routes (Frontend)
    re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]

# Service des médias uniquement en mode debug (local)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)