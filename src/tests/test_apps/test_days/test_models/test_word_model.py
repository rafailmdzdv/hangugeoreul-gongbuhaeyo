import random

import pytest

from server.apps.days import models


@pytest.mark.django_db()
def test_create_word() -> None:
    """This test checks that word creating successfully."""
    meaning, translation = ('알겠습니다', 'Понятно; ясно')
    random_study_day_title = random.SystemRandom().randint(1, 10)
    word = models.Word.objects.create(
        meaning=meaning,
        translation=translation,
        day=models.StudyDay.objects.create(
            title=random_study_day_title,
        ),
    )
    assert word.meaning == meaning
    assert word.day.title == random_study_day_title
