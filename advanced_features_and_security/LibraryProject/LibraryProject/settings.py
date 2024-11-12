from django.db import
from .models import CustomUser

class OtherModel(models.Model ):
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  ...
  bookshelf.CustomUser

#Set DEBUG to False in production DEBUG = False
#Browser-side protections
SECURE_BROWSER_XXS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = TRUE

#Enforce HTTPS-only cookies
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

#Additional security settings
SECURE_SSL_REDIRECT =True
SECURE_HSTS_SECOND = 3600
SECURE_HSTS_PRELOAD = True
SECURE_BROWSER_XSS_FILTER
