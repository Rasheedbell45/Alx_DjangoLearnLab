from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.SlugRelatedField(read_only=True, slug_field="username")
    recipient = serializers.SlugRelatedField(read_only=True, slug_field="username")
    target_repr = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ("id", "recipient", "actor", "verb", "target_repr", "unread", "timestamp")
        read_only_fields = ("id", "recipient", "actor", "verb", "target_repr", "timestamp")

    def get_target_repr(self, obj):
        # Human-readable target info
        if obj.target is None:
            return None
        try:
            return str(obj.target)
        except Exception:
            return None
