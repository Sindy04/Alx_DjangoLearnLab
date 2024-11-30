from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAuthenticated

class BookDetailView(APIView):
  def get(self, resquest, pk):
    #Logic to retrieve a book by ID goes here
    book = Book.objects.get(pk=pk)
    serializer = BookSerializer(book)
    return
    Response(serializer.data)

class BookCreateView(APIView):
  def post(self, request):
    #Logic to create a new book goes here
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid();
    serializer.save()
    return
    Response(serializer.data,status=201)
    return
    Response(serializer.errors,status =400)

class BookListView(APIView):

class BookUpdateView(APIView):

class BookDeleteView(APIView):


from django_filters import rest_framework
from rest_framework import generics
