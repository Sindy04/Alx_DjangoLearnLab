from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  permission_classes = [permissions.IsAuthenticated]

def perform_create(self,serializer):
  serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
  queryset = Comment.objects.all()
  serializer_class=CommentSerializer
  permission_classes =[permissions.IsAuthenticated]

def perform_create(self,serializer):
  serializer.save(author=self.request.user)

#Create a view in the posts app that generates

from rest_framework import status
from rest_framework.response import Response
from rest_frame.views import APIView
from .models import Post
from accounts.models import User

class FeedView(APIView):
  def get(self, request):
    followed_users = request.user.following.all()
    posts = Post.objects.filter(author__in=following_users).order_by('_created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.date)
