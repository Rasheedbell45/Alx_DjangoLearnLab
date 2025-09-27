from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# ✅ List all books (public read-only access)
class BookListView(generics.ListAPIView):
    """
    Retrieve a list of all books.
    Accessible to anyone (authenticated or not).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# ✅ Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single book by its ID.
    Accessible to anyone.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# ✅ Create a new book (restricted to authenticated users)
class BookCreateView(generics.CreateAPIView):
    """
    Create a new book entry.
    Only authenticated users can perform this action.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# ✅ Update an existing book (restricted)
class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing book.
    Only authenticated users can perform this action.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# ✅ Delete a book (restricted)
class BookDeleteView(generics.DestroyAPIView):
    """
    Delete an existing book.
    Only authenticated users can perform this action.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
