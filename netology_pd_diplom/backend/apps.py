from django.apps import AppConfig
from django.core.signals import request_finished


class BackendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend'

    def ready(self):

        from . import signals

        request_finished.connect(signals.password_reset_token_created)
        request_finished.connect(signals.new_user_registered_signal)
        request_finished.connect(signals.new_order_signal)
