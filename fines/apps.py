from django.apps import AppConfig


class FinesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fines'

    # def ready(self):
    #     from jobs import updater
    #     updater.start()
