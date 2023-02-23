
from django.contrib import admin
from django.urls import path, re_path
from .views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', fetch_clubs, name='home'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('add/', add, name='add'),
    path('logout/', logout, name='logout'),

]

HANDLER404 = 'unihub.views.custom_handler404'
HANDLER500 = 'unihub.views.custom_handler500'
HANDLER403 = 'unihub.views.custom_handler403'
HANDLER400 = 'unihub.views.custom_handler400'
