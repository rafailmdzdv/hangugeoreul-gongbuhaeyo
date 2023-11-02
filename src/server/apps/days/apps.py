from django.apps import AppConfig
from django.utils.translation import gettext_lazy


class DaysConfig(AppConfig):
    """`Days` application config."""

    name = 'server.apps.days'
    verbose_name = gettext_lazy('Study days')
