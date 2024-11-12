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

#bookshelf/views.py
from django.shortcuts import render, redirect
from .models import Book

@login_required
def book_list(request):
books = Book.objects.all() #Using Django's ORM
return render(request,'book_list.html',{'books':books})
@login_required
def book_detail(request,pk):
  book = Book.objects.get(pk=pk) #Using Django's ORM
  return render(request,'book_detail.html',{'book':book})
  from .forms import ExampleForm
  
