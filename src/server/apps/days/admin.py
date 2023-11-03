"""Admin settings for `User` model."""
from django.contrib import admin

from server.apps.days import models


class TabularWordAdmin(admin.TabularInline):
    """`Word` tabular representation in admin-panel."""

    model = models.Word


@admin.register(models.Word)
class WordAdmin(admin.ModelAdmin):
    """`Word` representation in admin-panel."""


@admin.register(models.StudyDay)
class StudyDayAdmin(admin.ModelAdmin):
    """`StudyDay` representation in admin-panel."""

    inlines = (TabularWordAdmin,)
