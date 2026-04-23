from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    # Administration
    path('doulgue/', admin.site.urls),
    
    # API endpoints (doivent être avant le catch-all)
    path('api/core/', include('apps.core.urls')),
    path('api/contact/', include('apps.contact.urls')),
]

# ⚠️ IMPORTANT : Servir les statiques AVANT le catch-all React
# WhiteNoise gère /static/, Django gère /media/ en dev
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Catch-all pour React SPA : EXCLUT explicitement /static/ et /media/
urlpatterns += [
    re_path(r'^(?!static/|media/|admin/|api/).*$', TemplateView.as_view(template_name='index.html')),
]