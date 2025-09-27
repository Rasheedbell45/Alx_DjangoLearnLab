from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    # ✅ List all books
    path("books/", BookListView.as_view(), name="book-list"),

    # ✅ Retrieve single book by ID
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),

    # ✅ Create new book
    path("books/create/", BookCreateView.as_view(), name="book-create"),

    # ✅ Update existing book
    path("books/update/<int:pk>/", BookUpdateView.as_view(), name="book-update"),

    # ✅ Delete existing book
    path("books/delete/<int:pk>/", BookDeleteView.as_view(), name="book-delete"),
]
