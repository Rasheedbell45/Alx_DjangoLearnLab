from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comment, Like

User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field="username")

    class Meta:
        model = Comment
        fields = ("id", "post", "author", "content", "created_at", "updated_at")
        read_only_fields = ("id", "author", "created_at", "updated_at")


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field="username")
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ("id", "author", "title", "content", "created_at", "updated_at", "comments", "comments_count")
        read_only_fields = ("id", "author", "created_at", "updated_at", "comments", "comments_count")

    def get_comments_count(self, obj):
        return obj.comments.count()

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field="username")
    class Meta:
        model = Like
        fields = ("id", "post", "user", "created_at")
        read_only_fields = ("id", "user", "created_at")
