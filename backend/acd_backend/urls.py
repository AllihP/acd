from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('doulgue/', admin.site.urls), # Admin secret
    path('api/core/', include('apps.core.urls')),
    path('api/contact/', include('apps.contact.urls')),

    # Sert l'index.html de React pour TOUTES les autres routes
    # Django cherchera ce fichier dans REACT_DIST_DIR défini dans settings.py
    re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]