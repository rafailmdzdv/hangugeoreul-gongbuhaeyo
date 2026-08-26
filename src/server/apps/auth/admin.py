# Copyright © 2026 Rafail Medzhidov <rafayt323@gmail.com>
# SPDX-License-Identifier: MIT

from typing import final

from django.contrib import admin

from server.apps.auth.models import User


@final
@admin.register(User)
class UserAdmin(admin.ModelAdmin[User]):
    list_display = ['email']
    search_fields = ['email']
