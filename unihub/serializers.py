from rest_framework import serializers
from .models import ClubCategory, Club, ClubEvent, ClubMember, ClubMeeting, UserProfile, UserClub
from django.contrib.auth.models import Group, User
from rest_framework.response import Response


class ClubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubCategory
        fields = '__all__'


class ClubSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    creator = serializers.ReadOnlyField(source='creator.username')
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    contact_email = serializers.EmailField(required=False)
    contact_phone = serializers.CharField(required=False)
    location = serializers.CharField(required=False)
    instagram = serializers.URLField(required=False)
    image = serializers.ImageField(required=False)
    constitution = serializers.FileField(required=False)
    category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Club
        fields = '__all__'


class ClubEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubEvent
        fields = ('id', 'title', 'description', 'start_date', 'end_date', 'location', 'creator')


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
