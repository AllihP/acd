from django.views.static import serve
import os

urlpatterns = [
    path('doulgue/', admin.site.urls), #
    path('api/core/', include('apps.core.urls')),
    
    # On sert l'index.html physique qui est maintenant dans staticfiles
    re_path(r'^.*$', serve, {
        'document_root': settings.STATIC_ROOT,
        'path': 'index.html'
    }),
]