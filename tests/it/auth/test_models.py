from typing import final

from hypothesis import given
from hypothesis import strategies as st
from hypothesis.extra import django

from server.apps.auth.models import User


@final
class TestUserModel(django.TestCase):
    @given(
        django.from_model(
            User,
            first_name=st.just('John'),
            source_language=st.one_of([st.just('ru'), st.just('en')]),
        ),
    )
    def test_model(self, instance: User) -> None:
        instance.save()

        assert instance.pk > 0
        assert instance.first_name == 'John'
        assert instance.source_language in ['ru', 'en']
