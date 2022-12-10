from django.apps import AppConfig

class UserprofileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userprofile'

    def ready(self):
        # noinspection PyUnresolvedReferences
        import userprofile.signals