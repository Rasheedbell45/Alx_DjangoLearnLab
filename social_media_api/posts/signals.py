from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Comment, Like
from django.contrib.contenttypes.models import ContentType
from notifications.models import Notification

@receiver(post_save, sender=Comment)
def notify_on_comment(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        if post.author != instance.author:
            Notification.objects.create(
                recipient=post.author,
                actor=instance.author,
                verb="commented on your post",
                target_content_type=ContentType.objects.get_for_model(post),
                target_object_id=str(post.id),
            )
