from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('doulgue/', admin.site.urls), # URL secrète
    path('api/core/', include('apps.core.urls')),
    path('api/contact/', include('apps.contact.urls')),
    
    # Catch-all pour le frontend React
    re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)