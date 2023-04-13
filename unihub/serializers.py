from rest_framework import serializers
from .models import ClubCategory, Club, ClubEvent, ClubMember, ClubMeeting, UserProfile, UserClub
from django.contrib.auth.models import Group, User


class ClubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubCategory
        fields = '__all__'


class ClubSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Club
        fields = '__all__'


class ClubEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubEvent
        fields = '__all__'


class ClubMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubMember
        fields = '__all__'


class ClubMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubMeeting
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserClub
        fields = '__all__'
