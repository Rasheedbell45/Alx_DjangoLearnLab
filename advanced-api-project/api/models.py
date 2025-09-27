from django.db import models

# Author model represents writers who can have multiple books
class Author(models.Model):
    name = models.CharField(max_length=255, help_text="Full name of the author")

    def __str__(self):
        return self.name


# Book model represents a book written by an Author
class Book(models.Model):
    title = models.CharField(max_length=255, help_text="Title of the book")
    publication_year = models.IntegerField(help_text="Year the book was published")
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books",  # Enables reverse lookup: author.books.all()
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
