from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

# becasue Django said so
    def ready(self):
        import users.signals
