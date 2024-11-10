"from django.db import models",
"class Author(models.Model)",
"return self.name"

"class Book(models.Model)", 
"title", "author"

"class Librarian(models.Model)",
"library"

"class UserProfile(models.Model):",
"ROLE_CHOICES = ("
('Admin','Admin'),
('Librarian','Librarian),
('Member","Member"),
)
 user = models.OneToOneField(User,on_delete=models.CASCADE)
 role = models.CharField(max_length=10, choice = ROLE_CHOICES,default = 'Member')                       

@receiver(post_save,sender = User)
def create_user_profile(sender,instance,created, *kwargs):
  if created:
    UserProfile.objects.create(user=instance)
    @receiver(post_save, sender=User)
    def save_user_profile(sender,instance,**kwargs):
      instance.userprofile.save()

"class Meta",
"permissions"



    
