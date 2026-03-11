from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import post_save
from toDoApp.profiles.models import ToDoProfile


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    if created:
        ToDoProfile.objects.create(
            user=instance,
            age=18,
            tasks=0,
        )

