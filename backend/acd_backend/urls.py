from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    # Votre accès secret pour l'admin
    path('doulgue/', admin.site.urls), 
    
    # Routes API
    path('api/core/', include('apps.core.urls')),
    path('api/contact/', include('apps.contact.urls')),
    
    # TOUTES les autres routes servent l'index de React
    re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]