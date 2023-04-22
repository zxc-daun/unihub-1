from django.contrib import admin
from django.urls import path, re_path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', FetchClubsView.as_view(), name='home'),
    path('add/', AddView.as_view(), name='add'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('about/', AboutView.as_view(), name='about'),
    path('accounts/', include('accounts.urls')),
    path('club/<slug:slug>/', ClubDetailView.as_view(), name='club_detail'),
    path('user_dashboard/', UserDashboardView.as_view(), name='user-dashboard'),
    path('club_admin_dashboard', views.ClubAdminDashboardView.as_view(), name='club_admin_dashboard'),
    path("create-club/", CreateClubView.as_view(), name="create-club"),
    path('club_follow/', ClubFollowView.as_view(), name='club_follow'),
    path('club/<slug:slug>/followers/', ShowClubFollowersView.as_view(), name='show-followers'),
    path('club/<slug:slug>/', ClubInfoView.as_view(), name='club-info'),
    path('edit_profile/', EditProfileView.as_view(), name='edit_profile'),
    path('create-event/', CreateEventView.as_view(), name='create-event'),
    path('club_events/<slug:slug>/', ClubEventListView.as_view(), name='club_events'),
    path('update-event/<int:event_id>/', views.update_event, name='update-event'),
    path('delete-event/<int:event_id>/', views.delete_event, name='delete-event'),
    path('complete-event/<int:event_id>/', views.complete_event, name='complete-event'),
    path('category/<str:category_slug>/', views.CategoryView.as_view(), name='category_view'),
    path('clubs/<int:pk>/', ClubViewSet.as_view({'delete': 'destroy'}), name='club-delete'),

    path('api/', include('unihub.api_urls')),
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
