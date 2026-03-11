from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    name = 'toDoApp.profiles'

    def ready(self):
        import toDoApp.profiles.signals


