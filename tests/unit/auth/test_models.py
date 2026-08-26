# Copyright © 2026 Rafail Medzhidov <rafayt323@gmail.com>
# SPDX-License-Identifier: MIT

from typing import final

from django.contrib.auth import get_user_model
from django.db import IntegrityError
from hypothesis import given
from hypothesis import strategies as st
from hypothesis.extra import django

from server.apps.auth.models import User

UserModel = get_user_model()


@final
class TestUserModel(django.TestCase):
    @given(
        django.from_model(
            User,
            first_name=st.just('John'),
            source_language=st.one_of([st.just('ru'), st.just('en')]),
            avatar=st.just(None),
        ),
    )
    def test_model(self, instance: User) -> None:
        instance.save()

        assert instance.pk > 0
        assert instance.first_name == 'John'
        assert instance.source_language in ['ru', 'en']

    def test_default_source_language(self) -> None:
        UserModel.objects.create_user(
            email='lang@example.com',
            password='pass123',
        )
        user = UserModel.objects.get(email='lang@example.com')
        assert user.source_language == User.Language.EN

    def test_username_field_is_email(self) -> None:
        assert User.USERNAME_FIELD == 'email'

    def test_email_normalized_on_clean(self) -> None:
        UserModel.objects.create_user(
            email='UPPER@EXAMPLE.COM',
            password='pass123',
        )
        user = UserModel.objects.get(email='UPPER@EXAMPLE.COM')
        user.email = '  MIXED@Example.COM  '
        user.clean()
        assert user.email == 'MIXED@example.com'

    def test_unique_email_constraint(self) -> None:
        UserModel.objects.create_user(
            email='dup@example.com',
            password='pass123',
        )
        with self.assertRaises(IntegrityError):  # noqa: PT027
            UserModel.objects.create_user(
                email='dup@example.com',
                password='pass456',
            )

    def test_blank_names_allowed(self) -> None:
        UserModel.objects.create_user(
            email='noname@example.com',
            password='pass123',
        )
        user = UserModel.objects.get(email='noname@example.com')
        assert user.first_name == ''
        assert user.last_name == ''


@final
class TestUserManager(django.TestCase):
    def test_create_user_sets_flags(self) -> None:
        UserModel.objects.create_user(
            email='regular@example.com',
            password='pass123',
        )
        user = UserModel.objects.get(email='regular@example.com')
        assert user.is_staff is False
        assert user.is_superuser is False
        assert user.pk is not None

    def test_create_superuser_sets_flags(self) -> None:
        UserModel.objects.create_superuser(
            email='admin@example.com',
            password='pass123',
        )
        user = UserModel.objects.get(email='admin@example.com')
        assert user.is_staff is True
        assert user.is_superuser is True
        assert user.pk is not None

    def test_create_user_hashes_password(self) -> None:
        UserModel.objects.create_user(
            email='hash@example.com',
            password='mypassword',
        )
        user = UserModel.objects.get(email='hash@example.com')
        assert user.password != 'mypassword'
        assert user.check_password('mypassword') is True

    def test_create_superuser_hashes_password(self) -> None:
        UserModel.objects.create_superuser(
            email='hashadmin@example.com',
            password='adminpass',
        )
        user = UserModel.objects.get(email='hashadmin@example.com')
        assert user.check_password('adminpass') is True
