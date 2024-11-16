relationship_app/list_books.html, 
Book.objects.all()
relationship_app/library_detail.html,
library, 
from .models import Library
from django.views.generic.detail import DetailView

from django.contrib.auth import login "
from django.contrib.auth.forms import UserCreationForm
UserCreationForm()
relationship_app/register.html

from django.contrib.auth.decorators import permission_required
relationship_app.can_add_book
relationship_app.can_change_book
relationship_app.can_delete_book


from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def admin_view(request):
  return render(request,'admin.html')

def librarian_view(request):
  return render(request, 'librarian.html')

def member_view(request):
  return render(request, 'member.html')

#Role checks
def is_admin(user):
  return user.userprofile.role =='Admin'

def is_librabrian(user):
  return user.userprofile.role == 'Librarian'

def is_member(user):
  return user.userprofile.role == 'Member'

#Apply role checks to views
admin_view = user_passes_test(is_admin)(admin_view)
librarian_view = user_passes_test(is_librarian)(librarian_view)
member_view = user_passes_test(is_member)(member_view)

def is_admin()
  #test logic
@user_passes_test(admin_test)
admin_view = user_passes_test(is_admin)(admin_view)
def admin_view(request)
#your view logic
return render(*args,*kwargs)

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
  if created:
    UserProfile.objects.create(user=instance)


#RELATIONSHIP
relationship_app/member_view.html
relationship_app/librarian_view.html
relationship_app/admin_view.html
