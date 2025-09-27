from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# ✅ List all books (open to everyone, read-only)
class BookListView(generics.ListAPIView):
    """
    Returns a list of all books.
    Open to both authenticated and unauthenticated users (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # anyone can read


# ✅ Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    """
    Returns details of a single book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # anyone can read


# ✅ Create a new book (restricted to authenticated users)
class BookCreateView(generics.CreateAPIView):
    """
    Allows authenticated users to add a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# ✅ Update an existing book
class BookUpdateVi
