INSTALLED_APPS = [
  ....
  'blog', Add this line
]
DATABASES={
  'default':{
  'ENGINE': 'django.db.backends.postgresql', #Use 'postgresql' for PostgreSQL
    'NAME': 'database_name', #Replace with your database name
    'USER': 'database_user', #Replace with your databse username
    'PASSWORD': 'database_password', #Replace with your database password
    'HOST':'localhost', #Replace with your database host
    'PORT':'5432', #Replace with your database port
  }
}
