"models.CharField", "max_length", "200", "title", "author"

from django.contrib.auth.models import AbstractUser
from django.db import models

#Class Custom user
Class CustomUser(AbstractUser):
date_of_birth = models.DateField(null=True, blank=True)
profile_photo = models.ImageField(upload_to = 'profile_photos/', null=True, blank=True)

def __str__(self):
  return self . username
