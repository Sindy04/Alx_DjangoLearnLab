from django.urls import path
from . import views

urlpatterns = [
  path('books/<int:pk>/',views.BookDetailView.as_view(),name='book-detail'),
  path('books/',views.BookCreateView.as_view(),name='book-create'),
  path('books/',views.BookCreate.as_view(),name= 'books/create'),
  path('books/',views.Bookupdate.as_view(0,name='books/update'),
  path('books/',views.Bookdelete.as_view(0,name='books/delete')
]
