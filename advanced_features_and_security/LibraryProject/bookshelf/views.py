from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Book

#Create your views here.

@permission_required('bookshelf .can_view_book', raise_exception=True)
def book_list(request):
  books = Book.objects.all()
  return render(request, 'book_list.html', {'books': books})

@permission_required('bookshelf.can_create_book', raise_exception=True)
def book_delete(request, pk)
#Book deletion logic here
return render(request, 'book_confirm_delete.html')
