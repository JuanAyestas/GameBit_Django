from django.apps import AppConfig


class UsersBitConfig(AppConfig):
    name = 'users_bit'
    
    def ready(self):
        import users_bit.signals
