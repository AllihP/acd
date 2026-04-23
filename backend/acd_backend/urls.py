from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.static import serve  # ← Pour servir /media/ en prod

urlpatterns = [
    path('doulgue/', admin.site.urls),
    path('api/core/', include('apps.core.urls')),
    path('api/contact/', include('apps.contact.urls')),
]

# ✅ Servir les fichiers médias (dev + prod)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]

# ✅ Catch-all React SPA : EXCLUT strictement static, media, api, admin, assets
urlpatterns += [
    re_path(r'^(?!static/|media/|api/|admin/|assets/|favicon\.ico).*$', 
            TemplateView.as_view(template_name='index.html')),
]