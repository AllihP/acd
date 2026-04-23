from django.views.generic import TemplateView
from django.urls import path, include, re_path

urlpatterns = [
    path('doulgue/', admin.site.urls), # Votre admin secret
    path('api/core/', include('apps.core.urls')),
    path('api/contact/', include('apps.contact.urls')),
    
    # On sert l'index.html qui se trouve dans STATIC_ROOT (celui collecté)
    re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]