from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITestCase(APITestCase):
    """
    Comprehensive tests for Book API endpoints including:
    - CRUD operations
    - Filtering, searching, ordering
    - Permissions enforcement
    """

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client = APIClient()

        # Create an author
        self.author = Author.objects.create(name="George Orwell")

        # Create test books
        self.book1 = Book.objects.create(
            title="1984", publication_year=1949, author=self.author
        )
        self.book2 = Book.objects.create(
            title="Animal Farm", publication_year=1945, author=self.author
        )

        # Endpoints
        self.list_url = reverse("book-list")
        self.create_url = reverse("book-create")
        self.detail_url = lambda pk: reverse("book-detail", args=[pk])
        self.update_url = lambda pk: reverse("book-update", args=[pk])
        self.delete_url = lambda pk: reverse("book-delete", args=[pk])

    # ----------------- CRUD Tests -----------------
    def test_list_books(self):
        """Test retrieving all books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book(self):
        """Test retrieving a single book"""
        response = self.client.get(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "1984")

    def test_create_book_unauthenticated(self):
        """Ensure unauthenticated users cannot create books"""
        response = self.client.post(
            self.create_url,
            {"title": "Homage to Catalonia", "publication_year": 1938, "author": self.author.id},
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        """Test authenticated user can create a book"""
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(
            self.create_url,
            {"title": "Homage to Catalonia", "publication_year": 1938, "author": self.author.id},
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Homage to Catalonia")

    def test_update_book_authenticated(self):
        """Test updating a book as authenticated user"""
        self.client.login(username="testuser", password="testpass")
        response = self.client.put(
            self.update_url(self.book1.id),
            {"title": "Nineteen Eighty-Four", "publication_year": 1949, "author": self.author.id},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Nineteen Eighty-Four")

    def test_delete_book_authenticated(self):
        """Test deleting a book as authenticated user"""
        self.client.login(username="testuser", password="testpass")
        response = self.client.delete(self.delete_url(self.book2.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book2.id).exists())

    # ----------------- Filtering / Search / Ordering Tests -----------------
    def test_filter_books_by_title(self):
        response = self.client.get(self.list_url, {"title": "1984"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "1984")

    def test_search_books(self):
        response = self.client.get(self.list_url, {"search": "Animal"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Animal Farm")

    def test_order_books_by_publication_year_desc(self):
        response = self.client.get(self.list_url, {"ordering": "-publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "1984")
        self.assertEqual(response.data[1]["title"], "Animal Farm")

    # ----------------- Permissions Tests -----------------
    def test_create_book_without_login(self):
        """Ensure unauthenticated user cannot create"""
        response = self.client.post(
            self.create_url,
            {"title": "Test Book", "publication_year": 2000, "author": self.author.id},
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
