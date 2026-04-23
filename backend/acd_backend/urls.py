from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

# Personnalisation de l'admin
admin.site.site_header = "ACD — Panneau d'Administration"
admin.site.site_title = "ACD Admin"
admin.site.index_title = "Tableau de Bord"

urlpatterns = [
    # Admin (Route protégée)
    path('doulgue/', admin.site.urls),
    
    # API Endpoints
    path('api/', include('apps.core.urls')),
    path('api/', include('apps.contact.urls')),
    
    # Catch-all pour React : Toutes les autres routes servent index.html
    re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]

# Service des médias en développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)