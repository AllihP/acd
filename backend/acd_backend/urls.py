from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    # Administration Unfold
    path('doulgue/', admin.site.urls),
    
    # API endpoints (DOIVENT être avant le catch-all)
    path('api/core/', include('apps.core.urls')),
    path('api/contact/', include('apps.contact.urls')),
]

# Servir les médias en développement uniquement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ⚠️ CATCH-ALL REACT : EXCLUT explicitement static/, media/, api/, admin/, assets/
# La regex (?!...) est une "negative lookahead" qui empêche la capture des fichiers statiques
urlpatterns += [
    re_path(r'^(?!static/|media/|api/|admin/|assets/|favicon\.ico).*$', 
            TemplateView.as_view(template_name='index.html')),
]