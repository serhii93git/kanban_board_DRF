from rest_framework import serializers
from .models import UserProfile, User


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for user profile model"""

    class Meta:
        model = UserProfile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user model"""

    class Meta:
        model = User
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for author main info as id, name, etc."""

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', ]
