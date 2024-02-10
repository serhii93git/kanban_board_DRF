from django.urls import path
from .views import UserProfileDetailView, UserProfileCreateView

urlpatterns = [
    path('profile/', UserProfileDetailView.as_view(), name='user-profile'),
]
