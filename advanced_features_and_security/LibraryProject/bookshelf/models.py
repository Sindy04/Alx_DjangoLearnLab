"models.CharField", "max_length", "200", "title", "author"

from django.contrib.auth.models import AbstractUser
from django.db import models


#Class Custom user
class CustomUser(AbstractUser):
date_of_birth = models.DateField(null=True, blank=True)
profile_photo = models.ImageField(upload_to = 'profile_photos/', null=True, blank=True)

def __str__(self):
  return self . username

from django.contrib.auth.models import BaseUserManager 
from django.utils import timezone

class CustomUserManager(BaseUserManager):
  def create_user(self, username, email, password=None, **extra_fields):
    if not username:
      raise ValueError('Users must have a username')
      if not email:
        raise ValueError('Users must have an email address')
                         
