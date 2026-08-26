# Copyright © 2026 Rafail Medzhidov <rafayt323@gmail.com>
# SPDX-License-Identifier: MIT

from typing import final

from django.apps import AppConfig


@final
class AuthConfig(AppConfig):
    name = 'server.apps.auth'
    label = 'authentication'
