from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
    path("register/", views.register_view, name="register"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("admin-view/", views.admin_view, name="admin_view"),
    path("librarian-view/", views.librarian_view, name="librarian_view"),
    path("member-view/", views.member_view, name="member_view"),
    path("books/", views.book_list, name="book_list"),
    path("books/add/", views.add_book, name="add_book"),
    path("books/edit/<int:book_id>/", views.edit_book, name="edit_book"),
    path("books/delete/<int:book_id>/", views.delete_book, name="delete_book"),
]
