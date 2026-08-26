# Copyright © 2026 Rafail Medzhidov <rafayt323@gmail.com>
# SPDX-License-Identifier: MIT

from http import HTTPStatus
from typing import Final

from django.urls import reverse
import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client
from PIL import Image
from io import BytesIO

from plugins.helpers import create_test_avatar, make_jwt_token

_USER_URL: Final = reverse('api:user:user')
_UPDATE_URL: Final = reverse('api:user:update_user')
_UPLOAD_AVATAR_URL: Final = reverse('api:user:upload_avatar')

_AUTH_HEADER: Final = 'HTTP_AUTHORIZATION'


def _auth_header(user_id: int) -> dict[str, str]:
    token = make_jwt_token(user_id)
    return {_AUTH_HEADER: f'Bearer {token}'}


@pytest.mark.django_db
def test_get_user_info(client: Client, create_user) -> None:
    client.post(
        _UPLOAD_AVATAR_URL,
        data={'avatar': create_test_avatar()},
        **_auth_header(create_user.pk),
    )
    response = client.get(_USER_URL, **_auth_header(create_user.pk))
    assert response.status_code == HTTPStatus.OK
    body = response.json()
    assert body['email'] == 'user@example.com'
    assert body['first_name'] == 'John'
    assert body['last_name'] == 'Doe'
    assert body['source_language'] == 'en'
    assert 'avatar_url' in body


@pytest.mark.django_db
def test_get_user_without_auth(client: Client) -> None:
    response = client.get(_USER_URL)
    assert response.status_code == HTTPStatus.UNAUTHORIZED


@pytest.mark.django_db
def test_get_user_with_invalid_token(client: Client) -> None:
    response = client.get(
        _USER_URL,
        **{_AUTH_HEADER: 'Bearer garbage.token.here'},
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED


@pytest.mark.django_db
def test_update_user_first_name(client: Client, create_user) -> None:
    response = client.patch(
        _UPDATE_URL,
        data={'first_name': 'Jane'},
        content_type='application/json',
        **_auth_header(create_user.pk),
    )
    assert response.status_code == HTTPStatus.OK
    body = response.json()
    assert body['success'] is True

    create_user.refresh_from_db()
    assert create_user.first_name == 'Jane'


@pytest.mark.django_db
def test_update_user_last_name(client: Client, create_user) -> None:
    response = client.patch(
        _UPDATE_URL,
        data={'last_name': 'Smith'},
        content_type='application/json',
        **_auth_header(create_user.pk),
    )
    assert response.status_code == HTTPStatus.OK

    create_user.refresh_from_db()
    assert create_user.last_name == 'Smith'


@pytest.mark.django_db
def test_update_user_source_language(client: Client, create_user) -> None:
    response = client.patch(
        _UPDATE_URL,
        data={'source_language': 'ru'},
        content_type='application/json',
        **_auth_header(create_user.pk),
    )
    assert response.status_code == HTTPStatus.OK

    create_user.refresh_from_db()
    assert create_user.source_language == 'ru'


@pytest.mark.django_db
def test_update_multiple_fields(client: Client, create_user) -> None:
    response = client.patch(
        _UPDATE_URL,
        data={
            'first_name': 'Alice',
            'last_name': 'Wonder',
            'source_language': 'ru',
        },
        content_type='application/json',
        **_auth_header(create_user.pk),
    )
    assert response.status_code == HTTPStatus.OK

    create_user.refresh_from_db()
    assert create_user.first_name == 'Alice'
    assert create_user.last_name == 'Wonder'
    assert create_user.source_language == 'ru'


@pytest.mark.django_db
def test_update_user_without_auth(client: Client) -> None:
    response = client.patch(
        _UPDATE_URL,
        data={'first_name': 'Hacker'},
        content_type='application/json',
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED


@pytest.mark.django_db
def test_upload_avatar(client: Client, create_user) -> None:
    response = client.post(
        _UPLOAD_AVATAR_URL,
        data={'avatar': create_test_avatar()},
        **_auth_header(create_user.pk),
    )
    assert response.status_code == HTTPStatus.CREATED
    body = response.json()
    assert 'avatar_url' in body

    create_user.refresh_from_db()
    assert create_user.avatar


@pytest.mark.django_db
def test_upload_avatar_without_auth(client: Client) -> None:
    response = client.post(
        _UPLOAD_AVATAR_URL,
        data={'avatar': create_test_avatar()},
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED
