import django
import os

# Setup Django environment (only if running outside `manage.py shell`)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


def run_queries():
    # Query all books by a specific author
    author_name = "Jane Austen"
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author.name}: {[book.title for book in books_by_author]}")

    # List all books in a library
    library_name = "Central Library"
    library = Library.objects.get(name=library_name)
    library_books = library.books.all()
    print(f"Books in {library.name}: {[book.title for book in library_books]}")

    # Retrieve the librarian for a library
    librarian = library.librarian
    print(f"Librarian for {library.name}: {librarian.name}")


if __name__ == "__main__":
    run_queries()
