"relationship_app/list_books.html", 
"Book.objects.all()"

"relationship_app/library_detail.html", "library", 
"from .models import Library"

"from django.views.generic.detail import DetailView"

#views for user login, logout, and registration
"from django.contrib.auth import login", 
"from django.contrib.auth.forms import UserCreationForm"

"views.register","LogoutView.as_view(template_name=","LoginView.as_view(template_name="

#Admin view
"from django.contrib.auth.decorators imports permission_required"
"from django.shortcuts import render"
@permission_required('myapp.is_admin')
def admin_view(request):
  return render(request, 'admin.html')
