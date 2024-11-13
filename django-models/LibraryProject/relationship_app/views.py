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
  
