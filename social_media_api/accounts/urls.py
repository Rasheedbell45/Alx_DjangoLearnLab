from django.urls import path
from .views import RegisterAPIView, LoginAPIView, ProfileAPIView, PublicProfileAPIView

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("profile/", ProfileAPIView.as_view(), name="profile"),
    path("users/<str:username>/", PublicProfileAPIView.as_view(), name="public-profile"),
]
