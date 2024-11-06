"from django.db import models",
"class Author(models.Model)",
"return self.name"

"class Book(models.Model)", 
"title", "author"

"class Librarian(models.Model)",
"library"

"class UserProfile(models.Model):",
"Admin", "Member"

from django.db import models
class MyModel(models.Model):
  #...
  class Meta:
    permissions = [
      ("is_admin", "Can access admin view")
    ]
