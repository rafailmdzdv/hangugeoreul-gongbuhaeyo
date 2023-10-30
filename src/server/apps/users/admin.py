from django.contrib import admin

from server.apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """`User` representation in admin-panel."""
