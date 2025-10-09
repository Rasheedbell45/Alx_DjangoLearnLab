from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import NotificationSerializer
from .models import Notification

class NotificationListAPIView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by("-timestamp")


class MarkNotificationReadAPIView(generics.UpdateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Notification.objects.all()
    lookup_field = "pk"

    def update(self, request, *args, **kwargs):
        notification = self.get_object()
        if notification.recipient != request.user:
            return Response({"detail": "Not allowed"}, status=status.HTTP_403_FORBIDDEN)
        notification.unread = False
        notification.save()
        return Response(self.get_serializer(notification).data, status=status.HTTP_200_OK)
