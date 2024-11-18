from rest_framework import generics
from .models import MyModel
from .serializers import MyModelSerializer
generics.ListAPIView
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
