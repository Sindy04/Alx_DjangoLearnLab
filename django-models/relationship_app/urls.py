"from .views import list_books", "LibraryDetailView", "path"
views.register",
"LogoutView.as_view(template_name=",
"LoginView.as_view(template_name="
"LoginView.as_view(template_name="

"from django.urls import path"
"from . import views"

urlpatterns = [
    path('admin/',views.admin_view, name = 'admin_view'),
]
