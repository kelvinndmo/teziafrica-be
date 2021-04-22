from django.apps import AppConfig


class TeziappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'teziapp'

# def ready(self):
#         import users.signals