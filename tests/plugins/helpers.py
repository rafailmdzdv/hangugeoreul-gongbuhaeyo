# Copyright © 2026 Rafail Medzhidov <rafayt323@gmail.com>
# SPDX-License-Identifier: MIT

from collections.abc import Iterator
from datetime import timedelta
from typing import Final, Literal

import jwt as pyjwt
import pytest
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone
from dmr.security.jwt.token import JWToken
from PIL import Image
from io import BytesIO

User: Final = get_user_model()
_TOKEN_TYPE = Literal['access', 'refresh']

DEFAULT_EMAIL: Final = 'user@example.com'
DEFAULT_PASSWORD: Final = 'testpass123'
_ALGORITHM: Final = 'HS256'


@pytest.fixture()
def create_user(transactional_db: None) -> Iterator[User]:
    User.objects.create_user(
        email=DEFAULT_EMAIL,
        password=DEFAULT_PASSWORD,
        first_name='John',
        last_name='Doe',
        source_language='en',
    )
    yield User.objects.get(email=DEFAULT_EMAIL)


@pytest.fixture()
def create_superuser(transactional_db: None) -> Iterator[User]:
    User.objects.create_superuser(
        email='admin@example.com',
        password=DEFAULT_PASSWORD,
        first_name='Admin',
        last_name='User',
    )
    yield User.objects.get(email='admin@example.com')


def make_jwt_token(
    user_id: int,
    *,
    token_type: _TOKEN_TYPE = 'access',
) -> str:
    from django.conf import settings as django_settings

    return JWToken(
        sub=str(user_id),
        exp=timezone.now() + timedelta(hours=1),
        jti='test-jti-id',
        extras={'type': token_type},
    ).encode(
        secret=django_settings.SECRET_KEY,
        algorithm=_ALGORITHM,
    )


def make_expired_jwt_token(
    user_id: int,
    *,
    token_type: _TOKEN_TYPE = 'access',
) -> str:
    from django.conf import settings as django_settings

    now = timezone.now()
    payload = {
        'sub': str(user_id),
        'exp': (now - timedelta(hours=1)).timestamp(),
        'iat': (now - timedelta(hours=2)).timestamp(),
        'jti': 'expired-test-jti',
        'type': token_type,
    }
    return pyjwt.encode(
        payload,
        key=django_settings.SECRET_KEY,
        algorithm=_ALGORITHM,
    )


def create_test_avatar() -> SimpleUploadedFile:
    image = Image.new('RGB', (100, 100), color='blue')
    buffer = BytesIO()
    image.save(buffer, format='PNG')
    buffer.seek(0)
    return SimpleUploadedFile('avatar.png', buffer.read(), content_type='image/png')
