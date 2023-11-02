"""Admin settings for `User` model."""
from django.contrib import admin

from server.apps.days.models import StudyDay


@admin.register(StudyDay)
class StudyDayAdmin(admin.ModelAdmin):
    """`StudyDay` representation in admin-panel."""
