from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# Personnalisation de l'interface Admin
admin.site.site_header = "ACD — Panneau d'Administration"
admin.site.site_title = "ACD Admin"
admin.site.index_title = "Tableau de Bord"

urlpatterns = [
    # Redirection de la racine vers l'admin pour éviter la 404 au démarrage
    path('', lambda request: redirect('admin/', permanent=False)),
    
    # Administration
    path('admin/', admin.site.urls),
    
    # API Routes - Séparées par namespace pour éviter les conflits
    path('api/core/', include('apps.core.urls')),
    path('api/contact/', include('apps.contact.urls')),
    
    # Documentation de l'API (Swagger UI) - Très recommandé
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
]

# Gestion des fichiers statiques et médias en développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    # En production, WhiteNoise gère les statiques, 
    # mais nous gardons les routes médias pour la flexibilité
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)