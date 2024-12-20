from django.urls import path
from . import views

urlpatterns = [
  path('login/', views.login_view, name='login'),
  path('logout/', views.logout_view, name='logout'),
  path('register/',views.register_view, name='register')
  path('profile/',views.register_view, name='profile')
  
from django.urls import path
from . import views

urlpatterns = [
  path('posts/', views.PostListView.as_view(), name='post_list'),
  path('posts/<int:pk>/',views.PostDetailView.as_view(), name='post_detail'),
  path('posts/new/',views.PostCreateView.as_view(), name='post_create'),
  path('posts/<int:pk>/edit/',views.PostUpdateView.as_view(), name='post_update'),
  path('posts/<int:pk>/delete/',views.PostDeleteView.as_view(), name ='post_delete'),
]
path(post/<int:pk>/delete/", "post/<int:pk>/update/", "post/new/)

from django.urls import path
from . import views

urlpatterns = [
  # ...
  path('tags/<slug:tag_slug>/',views.PostByTagListView.as_view(), name='post_by_tag'),
  # ...
]
comment/<int:pk>/update/, post/<int:pk>/comments/new/, comment/<int:pk>/delete/
