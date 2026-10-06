"""
URL configuration for ArSa project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('dates.urls')),
]

# Customize admin site
admin.site.site_header = "ArSa Administration"
admin.site.site_title = "ArSa Admin"
admin.site.index_title = "Welcome to ArSa Control Panel"

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
