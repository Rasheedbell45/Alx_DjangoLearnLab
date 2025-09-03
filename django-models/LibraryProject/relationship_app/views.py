from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Book, Library


# ---------------------------
# Function-Based View (Books)
# ---------------------------
def list_books(request):
    books = Book.objects.all()
    return render(request, "list_books.html", {"books": books})


# ---------------------------
# Class-Based View (Library Detail)
# ---------------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"

    def get_object(self):
        return get_object_or_404(Library, pk=self.kwargs["pk"])


# ---------------------------
# User Authentication Views
# ---------------------------

# User Registration
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")  # redirect to any page you want
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


# User Login
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("list_books")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


# User Logout
def logout_view(request):
    logout(request)
    return redirect("login")
