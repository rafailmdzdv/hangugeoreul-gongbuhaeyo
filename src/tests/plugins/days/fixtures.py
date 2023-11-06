import pytest

from server.apps.days.models import StudyDay


@pytest.fixture()
def study_day() -> StudyDay:
    """This fixture creates a test study day."""
    return StudyDay.objects.create(title=1)
