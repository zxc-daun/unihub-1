
from django.contrib import admin
from django.urls import path, re_path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', fetch_clubs, name='home'),
    path('add/', add, name='add'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('accounts/', include('accounts.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

HANDLER404 = 'unihub.views.custom_handler404'
HANDLER500 = 'unihub.views.custom_handler500'
HANDLER403 = 'unihub.views.custom_handler403'
HANDLER400 = 'unihub.views.custom_handler400'
