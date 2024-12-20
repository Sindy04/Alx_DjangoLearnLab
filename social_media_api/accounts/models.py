from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
  bio = models.TextField(blank=True)
  profile_picture = models.ImageField(upload_to='profile_pictures/',blank=True)
  followers= models.ManyToManyField('self',symmetrical=False,blank=True)
  
#Implementing User Follows and Feed Functionality
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  following = models.ManyToManyField('self',symmetrical=False, blank=True)
  
