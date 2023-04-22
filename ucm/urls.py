
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from unihub.views import CustomHandler404View, CustomHandler500View, CustomHandler403View, CustomHandler400View

urlpatterns = [
    # path("admin/", admin.site.urls),
    path('admin-panel/', admin.site.urls, name='admin_panel'),
    path('', include('unihub.urls')),
    path('captcha/', include('captcha.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/', include('unihub.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = CustomHandler404View.as_view()
handler500 = CustomHandler500View.as_view()
handler403 = CustomHandler403View.as_view()
handler400 = CustomHandler400View.as_view()
