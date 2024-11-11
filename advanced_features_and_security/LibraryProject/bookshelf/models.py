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

      now = timezone.now()
      email = self . normalize_email(email)
      user = self . model(
        username=username,
        email=email,
        date_of_birth=extra_fields.pop('date_of_birth', None),
        profile_photo=extra_fields.pop('profile_photo', None),

        is_staff=False
        is_active=True
        is_superuser=False,
        last_login=now,
        date_joined=now,
         **extra fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
      
def create_superuser(self, username, email, password=None, **extra_fields):
  user = self.create_user(
    username=username,
    email=email,
    password=password,
    **extra_fields
  )
  user.is_staff =True
  user.is_superuser = True
  user.save(using=self._db)
  return user

class CustomUser(AbstractUser):
  ...
  objectd = CustomUserManager()


# File Existence and Custom Permissions

from django.db import models

class Mymode(models.Model):
  #...
  class Meta:'
    permissions = [
      ("can_view", "can view my model")'
      ("can_create", "can create my model"),
      ("can_edit"< "can edit my model"),
      ("can_delete", "can delete my model"),
    ]

