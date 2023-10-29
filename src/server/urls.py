"""Main URL mapping configuration file."""

import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.contrib.admindocs import urls as admindocs_urls
from django.urls import include, path
from health_check import urls as health_urls

admin.autodiscover()

urlpatterns = [
    # Health checks:
    path('health/', include(health_urls)),

    # django-admin:
    path('admin/doc/', include(admindocs_urls)),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:

    urlpatterns = [
        # URLs specific only to django-debug-toolbar:
        path('__debug__/', include(debug_toolbar.urls)),
        *urlpatterns,
    ]
