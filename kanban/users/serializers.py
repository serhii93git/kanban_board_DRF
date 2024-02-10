from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for user profile model"""

    class Meta:
        model = UserProfile
        fields = '__all__'
