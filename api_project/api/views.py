from rest_framework import generics
from .models import MyModel
from .serializers import MyModelSerializer
generics.ListAPIView
from .serializers import BookSerializer

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

router .register(r'book_all' , BookViewSet, basename='book_all')

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MyModelViewSet

router = DefaultRouter()
router.register(r'my-models', MyModelViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
