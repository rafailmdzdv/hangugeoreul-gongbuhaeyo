from django.apps import AppConfig
from django.utils.translation import gettext_lazy


class UsersConfig(AppConfig):
    """`Users` application config."""

    name = 'server.apps.users'
    verbose_name = gettext_lazy('users')
