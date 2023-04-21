from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

from .views import CreateEventView

router = DefaultRouter()
router.register(r'club_categories', views.ClubCategoryViewSet)
router.register(r'clubs', views.ClubViewSet)
router.register(r'club_members', views.ClubMemberViewSet)
router.register(r'club_meetings', views.ClubMeetingViewSet)
router.register(r'user_profiles', views.UserProfileViewSet)
router.register(r'user_clubs', views.UserClubViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #path('login/', views.LoginApiView.as_view(), name='api-login'),
    #path('clubs/', views.ClubListAPIView.as_view(), name='club_list_api'),
]
