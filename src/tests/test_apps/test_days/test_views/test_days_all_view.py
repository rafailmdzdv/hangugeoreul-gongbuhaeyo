import http

import pytest
from django.test import Client
from django.urls import reverse

from server.apps.days.models import StudyDay


@pytest.mark.django_db()
def test_days_all_api(client: Client, study_day: StudyDay) -> None:
    """This test checks that getting all study days is working successfuly."""
    response = client.get(reverse('days:all-days'))
    assert http.HTTPStatus.OK == response.status_code
    assert response.json()[-1]['title'] == 1
