from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.http import JsonResponse, HttpResponse

def api_root_view(request):
    return JsonResponse({
        "status": "success",
        "message": "ACD Backend API is running perfectly!",
        "endpoints": {
            "admin": "/doulgue/",
            "core": "/api/core/",
            "contact": "/api/contact/"
        }
    })

def favicon_view(request):
    return HttpResponse(status=204)  # No content

urlpatterns = [
    path('', api_root_view, name='api_root'),
    path('favicon.ico', favicon_view),
    path('doulgue/', admin.site.urls),
    path('api/core/', include('apps.core.urls')),
    path('api/contact/', include('apps.contact.urls')),
]

# ✅ Servir les médias (dev + prod temporaire)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]