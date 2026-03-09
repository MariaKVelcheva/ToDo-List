from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    name = 'toDoApp.accounts'

    def ready(self):
        import toDoApp.accounts.signals


