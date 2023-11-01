import datetime

import pytest

from server.apps.users.models import User


@pytest.mark.django_db()
def test_create_user() -> None:
    """This test checks that user is creating successfully."""
    email, password = ('a@a.ru', '123')
    user = User.objects.create(
        email=email,
        password=password,
        date_birth=datetime.date.today(),
    )
    assert user.password == password
