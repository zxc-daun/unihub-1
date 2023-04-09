from django.contrib import admin
from django.urls import path, re_path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #
    path("admin/", admin.site.urls),
    # path('admin-panel/', admin.site.urls, name='admin_panel'),
    path('', FetchClubsView.as_view(), name='home'),
    path('add/', AddView.as_view(), name='add'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('about/', AboutView.as_view(), name='about'),
    path('accounts/', include('accounts.urls')),
    path('club/<slug:slug>/', ClubDetailView.as_view(), name='club_detail'),
    path('user_dashboard/', UserDashboardView.as_view(), name='user-dashboard'),
    path('club_admin_dashboard/', ClubAdminDashboardView.as_view(), name='club_admin_dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      re_path(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns


handler404 = CustomHandler404View.as_view()
handler500 = CustomHandler500View.as_view()
handler403 = CustomHandler403View.as_view()
handler400 = CustomHandler400View.as_view()
