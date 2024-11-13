from django.db import models

class Author(models.Model):
  name = models.CharField(max_length=100)'

class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Library(models.Model):
  name = models.CharField(max_length=100)
  books = models.ManyToManyField(Book)

class Librarian(models.Model):
  name = models.CharField(max_length=100)
  library =models.OneToOneField(Library,on_delete=models.CASCADE)
  return self.name

class Meta:
permissions
can_add_book, can_change_book, can_delete_book

class UserProfile(models.Model):
  Admin, Member

from django.db import models
from django.contrib.auth.models import user

ROLE_CHOICES = [
  ('Admin','Admin')
  ('Librarian','Librarian')
  ('Member','Member')
]
class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE)
  role = models.CharField(max_length=10, choices = ROLE_CHOICES)

def __str__(self):
  return self.user.username
