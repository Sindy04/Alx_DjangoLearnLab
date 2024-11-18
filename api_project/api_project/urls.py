pythonCopy codefrom django.urls import path
from .views import BookListCreateAPIView
api.urls
urlpatterns = [
    path("api/books", views.BookListCreateAPIView.as_view(), name="book_list_create"),
]
