"""Module with models to representate days."""
from typing import Final

from django.db import models
from django.utils.translation import gettext_lazy

from server.settings.components.fields import DEFAULT_ID_PARAMS

_MEANING_LENGTH: Final = 40
_TRANSLATION_LENGTH: Final = 70


class StudyDay(models.Model):
    """StudyDay model with required fields."""

    id = models.UUIDField(**DEFAULT_ID_PARAMS)
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


class Word(models.Model):
    """Word of study day with required fields."""

    id = models.UUIDField(**DEFAULT_ID_PARAMS)
    meaning = models.CharField(
        max_length=_MEANING_LENGTH,
        verbose_name=gettext_lazy('Meaning'),
        blank=False,
    )
    translation = models.CharField(
        max_length=_TRANSLATION_LENGTH,
        verbose_name=gettext_lazy('Translation'),
        blank=False,
    )
    day = models.ForeignKey(
        StudyDay,
        verbose_name=gettext_lazy('Day'),
        related_name='words',
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'words'
        verbose_name = gettext_lazy('Word')
        verbose_name_plural = gettext_lazy('Words')

    def __str__(self) -> str:
        """String representation of word with it's korean meaning."""
        return self.meaning
