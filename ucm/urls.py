
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path("admin/", admin.site.urls),
    path('admin-panel/', admin.site.urls, name='admin_panel'),
    path('', include('unihub.urls')),
    path('accounts/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


