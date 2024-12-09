from rest_framework import status
from rest_framework.response import Rosponse
from rest_framework.views import APIView
from .models import User

class FollowUserView(APIView):
  def post(self, request, user_id):
    user_to_follow = User.objects.get(id=user_id)
    request.user.following.add(user_to_follow)
    return Response(status=status.HTTP_201_CREATED)

class UnfollowUserView(APIView):
  def post(self,request,user_id):
    user_to_unfollow = User.objects.get(id=user_id)
    request.user.following.remove(user_to_unfollow)
    return Response(status=status.HTTP_200_0k)
