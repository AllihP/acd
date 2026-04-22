from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Fonction simple pour que la racine du backend soit neutre
def home_view(request):
    return HttpResponse("ACD API Service", content_type="text/plain")

urlpatterns = [
    # On change l'URL de l'admin pour la cacher (mettez ce que vous voulez ici)
    path('doulgue/', admin.site.urls), 
    
    # Racine neutre (pas de redirection, pas d'accès admin visible)
    path('', home_view),
    
    # Points d'accès API pour le Frontend
    path('api/core/', include('apps.core.urls')),
    path('api/contact/', include('apps.contact.urls')),
]