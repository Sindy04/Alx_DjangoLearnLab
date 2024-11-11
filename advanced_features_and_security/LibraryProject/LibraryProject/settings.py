from django.db import
from .models import CustomUser

class OtherModel(models.Model ):
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  ...
  
