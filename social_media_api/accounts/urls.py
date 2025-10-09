from django.urls import path
from .views import RegisterAPIView, LoginAPIView, ProfileAPIView, PublicProfileAPIView, FollowUserAPIView, UnfollowUserAPIView, FollowersListAPIView, FollowingListAPIView

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("profile/", ProfileAPIView.as_view(), name="profile"),
    path("users/<str:username>/", PublicProfileAPIView.as_view(), name="public-profile"),
    path("follow/<int:user_id>/", FollowUserAPIView.as_view(), name="follow-user"),
    path("unfollow/<int:user_id>/", UnfollowUserAPIView.as_view(), name="unfollow-user"),
    path("users/<int:user_id>/followers/", FollowersListAPIView.as_view(), name="user-followers"),
    path("users/<int:user_id>/following/", FollowingListAPIView.as_view(), name="user-following"),
]
