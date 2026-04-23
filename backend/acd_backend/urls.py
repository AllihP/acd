from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    path('doulgue/', admin.site.urls),
    path('api/core/', include('apps.core.urls')),
    
    # 1. Servir les fichiers statiques explicitement s'ils sont demandés à la racine
    re_path(r'^assets/(?P<path>.*)$', serve, {'document_root': os.path.join(settings.REACT_DIST_DIR, 'assets')}),
    
    # 2. Le reste va vers React
    re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]