import random

import pytest

from server.apps.days.models import StudyDay


@pytest.mark.django_db()
def test_create_study_day() -> None:
    """This test checks that study day creating successfully."""
    random_title = random.SystemRandom().randint(1, 10)
    study_day = StudyDay.objects.create(
        title=random_title,
    )
    assert study_day.title == random_title
