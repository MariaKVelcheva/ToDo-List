from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class Category(models.Model):
        name = models.CharField(
            max_length=15,
        )


class Task(models.Model):
    CHOICES = (
        ("Done", "Done"),
        ("Not done", "Not done"),
    )

    title = models.CharField(
        max_length=30,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    assignee = models.ManyToManyField(
        to=UserModel,
        related_name="assigned_tasks",
        blank=True,
    )

    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        related_name='tasks',
    )

    state = models.CharField(
        max_length=30,
        choices=CHOICES,
        default='Not done',
    )

    def __str__(self):
        return self.title