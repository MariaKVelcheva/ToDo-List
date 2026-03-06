from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class EmailOrUsernameBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(get_user_model().USERNAME_FIELD)

        try:
            user = get_user_model().objects.get(email=username)
        except get_user_model().DoesNotExist:
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user

