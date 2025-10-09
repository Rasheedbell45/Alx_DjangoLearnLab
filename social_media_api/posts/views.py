from rest_framework import viewsets, permissions, filters, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    """
    list, retrieve, create, update, partial_update, destroy
    Supports search by title/content and ordering.
    """
    queryset = Post.objects.all().select_related("author").prefetch_related("comments")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = []  # e.g., ["author__username"]
    search_fields = ["title", "content"]
    ordering_fields = ["created_at", "updated_at"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # optional: list comments for a post via nested endpoint
    @action(detail=True, methods=["get"], permission_classes=[permissions.AllowAny])
    def comments(self, request, pk=None):
        post = self.get_object()
        comments = post.comments.all()
        page = self.paginate_queryset(comments)
        serializer = CommentSerializer(page or comments, many=True)
        if page is not None:
            return self.get_paginated_response(serializer.data)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    """
    CRUD for comments. Only author can update/delete.
    When creating a comment, ensure the user is the author.
    """
    queryset = Comment.objects.all().select_related("author", "post")
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["content"]
    filterset_fields = ["post__id"]  # filter by post id via ?post__id=2

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # posts from users current user follows
        user = self.request.user
        # user.following is already a queryset of User objects
        following_qs = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by
