"from .views import list_books", "LibraryDetailView", "path"
views.register",
"LogoutView.as_view(template_name=",
"LoginView.as_view(template_name="
"LoginView.as_view(template_name="

"from django.urls import path"
"from . import views"

urlpatterns = [
    path('Admin/',views.Admin_view, name = 'Admin_view'),
    path('Librarian/',views.Librarian_view, name = 'Librarian_view'),
    path('Member/' ,views.Member_view, name = 'Member_view'),
]
