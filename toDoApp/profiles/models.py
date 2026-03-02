from django.contrib.auth import models as auth_models, get_user_model
from django.db import models

from toDoApp.profiles.managers import ToDoManager


class ToDoUser(auth_models.AbstractUser):
    objects = ToDoManager()


