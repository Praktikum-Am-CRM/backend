from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from backend.swagger_utils import SchemaGenerator

schema_view = get_schema_view(
    openapi.Info(
        title='Yandex Ambassador CRM API',
        default_version='v1',
        description='Описание API endpoint for Yandex Ambassador',
        contact=openapi.Contact(email='admin@kittygram.ru'),
        license=openapi.License(name='MIT License'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    generator_class=SchemaGenerator,
)

urlpatterns = [
    path('api/v1/', include('api.urls', namespace='api_v1')),
    path('admin/', admin.site.urls),
    path(
        'docs/export/',
        schema_view.without_ui(cache_timeout=0),
        name='docs_export',
    ),
    path(
        'docs/', schema_view.with_ui('swagger', cache_timeout=0), name='docs'
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
