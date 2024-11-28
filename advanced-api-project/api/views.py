from rest_framework.response import Response
from rest_framework.views import APIView

class BookDetailView(APIView):
  def get(self, resquest, pk):
    #Logic to retrieve a book by ID goes here
    book = Book.objects.get(pk=pk)
    serializer = BookSerializer(book)
    return
    Response(serializer.data)

class
