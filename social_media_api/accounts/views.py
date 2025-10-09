from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from .models import Post  # assuming Post is accessible here

CustomUser = get_user_model()


# Registration View using GenericAPIView
class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    queryset = CustomUser.objects.all()  # Required line

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        data = UserSerializer(user, context={"request": request}).data
        return Response(
            {"user": data, "token": token.key},
            status=status.HTTP_201_CREATED
        )


# Login View
class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, _ = Token.objects.get_or_create(user=user)
        data = UserSerializer(user, context={"request": request}).data
        return Response(
            {"user": data, "token": token.key},
            status=status.HTTP_200_OK
        )


# Authenticated Profile View
class ProfileAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(serializer.data)

    def put(self, request):
        serializer = UserSerializer(
            request.user,
            data=request.data,
            partial=True,
            context={"request": request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# Public Profile
class PublicProfileAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, username):
        user = get_object_or_404(CustomUser, username=username)
        serializer = UserSerializer(user, context={"request": request})
        return Response(serializer.data)


# Follow / Unfollow
class FollowUserAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        if request.user.id == user_id:
            return Response({"detail": "You cannot follow yourself."},
                            status=status.HTTP_400_BAD_REQUEST)
        target = get_object_or_404(CustomUser, id=user_id)
        request.user.following.add(target)
        return Response({"detail": f"You are now following {target.username}."},
                        status=status.HTTP_200_OK)


class UnfollowUserAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        if request.user.id == user_id:
            return Response({"detail": "You cannot unfollow yourself."},
                            status=status.HTTP_400_BAD_REQUEST)
        target = get_object_or_404(CustomUser, id=user_id)
        request.user.following.remove(target)
        return Response({"detail": f"You unfollowed {target.username}."},
                        status=status.HTTP_200_OK)


# Followers / Following Lists
class FollowersListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        user = get_object_or_404(CustomUser, id=user_id)
        return user.followers.all()


class FollowingListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        user = get_object_or_404(CustomUser, id=user_id)
        return user.following.all()
