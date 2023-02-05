from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "backend_greenie.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import backend_greenie.users.signals  # noqa F401
        except ImportError:
            pass
