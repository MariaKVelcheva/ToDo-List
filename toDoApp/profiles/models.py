from django.contrib.auth import models as auth_models, get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from toDoApp.profiles.managers import ToDoManager


class ToDoUser(auth_models.AbstractUser):
    username = models.CharField(
        _("Username"),
        unique=True,
        max_length=150,
    )

    email = models.EmailField(
        _("Email address"),
        unique=True,
        max_length=254,
    )

    is_active = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)

    objects = ToDoManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class ToDoProfile(models.Model):
    user = models.OneToOneField(
        to=ToDoUser,
        on_delete=models.CASCADE,
        related_name='profile',
        primary_key=True,
    )

    age = models.IntegerField(default=0)

    tasks = models.IntegerField(default=0)
