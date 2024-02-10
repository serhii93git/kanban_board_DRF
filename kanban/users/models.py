from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """A model for user"""

    pass


class UserProfile(models.Model):
    """A model for user profile"""

    user = models.OneToOneField(to=User, on_delete=models.CASCADE, verbose_name='user',
                                help_text='link with User model')
    profile_image = models.ImageField(upload_to='profile_image/', verbose_name='profile image',
                                      help_text='add user photo')
    first_name = models.CharField(max_length=50, verbose_name='user name', help_text='your name')
    second_name = models.CharField(max_length=50, verbose_name='user surname', help_text='your surname')
    bio = models.TextField(verbose_name='user BIO', help_text='something about your self')

    def __str__(self):
        return f'{self.first_name} "{self.user.username}" {self.second_name} profile'
