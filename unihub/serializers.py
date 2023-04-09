from rest_framework import serializers
from .models import ClubCategory, Club, ClubEvent, ClubMember, ClubMeeting, UserProfile, UserClub


class ClubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubCategory
        fields = '__all__'


class ClubSerializer(serializers.ModelSerializer):
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
