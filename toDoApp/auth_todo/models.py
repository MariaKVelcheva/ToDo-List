from django.db import models


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