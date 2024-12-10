INSTALLED_APPS =[
  ...
  'rest_framework',
  'accounts',
]

INSTALLED_APPS=[
  ...
  'rest_framework',
  'posts',
]

DEBUG = False
ALLOWED_HOSTS

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'your-database-name',
    'USER': 'your-database-user',
    'PASSWORD': 'your-database-password'
    'HOST':  'your-database-host'
    'PORT': '5432'
  }
}
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
  
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFileStorage'

MIDDLEWARE = [
  #...
'whitenoise.middleware.WhiteNoiseMiddleware',
  #...
]
