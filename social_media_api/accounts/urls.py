from django.urls import path
from . import views

urlpatterns =[
  path('register/',views.RegisterView.as_view(), name='register')
  path('login/',views.LoginView.as_view(), name='login')
  path('profile/',views.ProfileView.as_view(), name='profile')

  #Checks for “Set up URL patterns in accounts/urls.py for follow management
  from django.urls import path
  from . import views
 urlpatterns = [
   path('follow/<int:user_id>/',views.FollowUserView.as_view(), name='follow_user'),
   path('unfollow/<int:user_id>/',views.UnfollowUserView.as_view(), name='unfollow_user'),
 ]
  urls
