from django.contrib import admin
from django.urls import path, re_path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'club_categories', views.ClubCategoryViewSet)
router.register(r'clubs', views.ClubViewSet)
router.register(r'club_events', views.ClubEventViewSet)
router.register(r'club_members', views.ClubMemberViewSet)
router.register(r'club_meetings', views.ClubMeetingViewSet)
router.register(r'user_profiles', views.UserProfileViewSet)
router.register(r'user_clubs', views.UserClubViewSet)


urlpatterns = [
    #
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),
    # path('admin-panel/', admin.site.urls, name='admin_panel'),
    path('api/login/', LoginApiView.as_view(), name='api-login'),
    path('api/api/clubs/', views.ClubListAPIView.as_view(), name='club_list_api'),
    path('', FetchClubsView.as_view(), name='home'),
    path('add/', AddView.as_view(), name='add'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('about/', AboutView.as_view(), name='about'),
    path('accounts/', include('accounts.urls')),
    path('club/<slug:slug>/', ClubDetailView.as_view(), name='club_detail'),
    path('user_dashboard/', UserDashboardView.as_view(), name='user-dashboard'),
    path('club_admin_dashboard/', views.ClubAdminDashboardView.as_view(), name='club_admin_dashboard'),
    # path('club_user_dashboard/', views.ClubDashboardView.as_view(), name='club_user_dashboard'),
    path("create-club/", CreateClubView.as_view(), name="create-club"),
    # path('update_club_data/', views.UpdateClubDataView.as_view(), name='update_club_data'),
    # path('api/clubs/<int:pk>/', views.ClubUpdateView.as_view(), name='club_update'),
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
