from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from apps.common.views import health_check

admin.site.site_header = "Erick Portfolio"
admin.site.site_title = "Panel de administración"
admin.site.index_title = "Gestión del portfolio"
admin.site.enable_nav_sidebar = False

urlpatterns = [
    path(
        settings.ADMIN_URL,
        admin.site.urls,
    ),
    path(
        "api/health/",
        health_check,
        name="health-check",
    ),
    path(
        "api/v1/",
        include("apps.portfolio.api.urls"),
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )