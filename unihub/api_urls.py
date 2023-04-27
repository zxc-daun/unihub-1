from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'club_categories', views.ClubCategoryViewSet)
router.register(r'clubs', views.ClubViewSet, basename='club')
router.register(r'club_members', views.ClubMemberViewSet)
router.register(r'club_meetings', views.ClubMeetingViewSet)
router.register(r'user_profiles', views.UserProfileViewSet)
router.register(r'user_clubs', views.UserClubViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
]
