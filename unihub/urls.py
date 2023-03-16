from django.contrib import admin
from django.urls import path, re_path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('admin-panel/', admin.site.urls, name='admin_panel'),
    path('', FetchClubsView.as_view(), name='home'),
    path('add/', AddView.as_view(), name='add'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('accounts/', include('accounts.urls')),
    path('categories/', HomeView.as_view(), name='home'),
    path('club/<slug:slug>/', ClubDetailView.as_view(), name='club_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = CustomHandler404View.as_view()
handler500 = CustomHandler500View.as_view()
handler403 = CustomHandler403View.as_view()
handler400 = CustomHandler400View.as_view()
