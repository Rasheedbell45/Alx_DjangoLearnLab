from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    """Form for creating and editing Book objects with validation."""
    class Meta:
        model = Book
        fields = ["title", "author", "published_date"]

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, help_text="Enter your full name")
    email = forms.EmailField(required=True, help_text="Enter a valid email address")
    message = forms.CharField(
        widget=forms.Textarea,
        required=True,
        help_text="Enter your message"
    )
