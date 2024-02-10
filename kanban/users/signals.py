from allauth.account.signals import user_signed_up
from django.dispatch import receiver

from .models import UserProfile


@receiver(user_signed_up)
def handle_user_signed_up(sender, request, user, **kwargs):
    """Signal for automatic creation user profile after sign up"""

    UserProfile.objects.create(user=user)
