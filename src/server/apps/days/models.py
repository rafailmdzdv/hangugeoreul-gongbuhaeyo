"""Module with models to representate days."""
import uuid

from django.db import models
from django.utils.translation import gettext_lazy


class StudyDay(models.Model):
    """StudyDay model with required fields."""

    id = models.UUIDField(
        verbose_name=gettext_lazy('Id'),
        primary_key=True,
        default=uuid.uuid4,
    )
    title = models.IntegerField(
        verbose_name=gettext_lazy('Title'),
        unique=True,
        db_index=True,
    )

    class Meta:
        db_table = 'study_days'
        verbose_name = gettext_lazy('Study day')
        verbose_name_plural = gettext_lazy('Study days')

    def __str__(self) -> str:
        """String representation of study day with day's number."""
        return 'Day №{0}'.format(self.title)
