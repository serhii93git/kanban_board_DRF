from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated
from .serializers import UserProfileSerializer
from .models import UserProfile


class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    """Detail view for user profile"""

    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)


class UserProfileCreateView(CreateAPIView):
    """Create view for user profile"""

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
