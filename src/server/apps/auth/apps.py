from typing import final

from django.apps import AppConfig


@final
class AuthConfig(AppConfig):
    name = 'server.apps.auth'
    label = 'authentication'
