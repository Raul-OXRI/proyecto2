from django.apps import AppConfig


class ModuloUsuarioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modulo_usuario'


    def ready(self):
        import modulo_usuario.signals