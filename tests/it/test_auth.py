# Copyright © 2026 Rafail Medzhidov <rafayt323@gmail.com>
# SPDX-License-Identifier: MIT

from http import HTTPStatus
from typing import Final

import pytest
from django.test import Client
from django.urls import reverse
from plugins.auth import make_expired_jwt_token, make_jwt_token

_OBTAIN_URL: Final = reverse('api:auth:authenticate')
_VERIFY_URL: Final = reverse('api:auth:verify_access_token')
_REFRESH_URL: Final = reverse('api:auth:refresh_token')
_LOGOUT_URL: Final = reverse('api:auth:logout')

_AUTH_HEADER: Final = 'HTTP_AUTHORIZATION'


def _auth_headers(user_id: int) -> dict[str, str]:
    token = make_jwt_token(user_id, token_type='access')
    return {_AUTH_HEADER: f'Bearer {token}'}


@pytest.mark.django_db
def test_obtain_tokens_success(client: Client, create_user) -> None:
    response = client.post(
        _OBTAIN_URL,
        data={'email': 'user@example.com', 'password': 'testpass123'},
        content_type='application/json',
    )
    body = response.json()

    assert 'access_token' in body
    assert 'refresh_token' in body


@pytest.mark.django_db
def test_obtain_tokens_wrong_password(client: Client, create_user) -> None:
    response = client.post(
        _OBTAIN_URL,
        data={'email': 'user@example.com', 'password': 'wrongpassword'},
        content_type='application/json',
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED  # noqa: WPS204


@pytest.mark.django_db
def test_obtain_tokens_nonexistent_user(client: Client) -> None:
    response = client.post(
        _OBTAIN_URL,
        data={'email': 'nobody@example.com', 'password': 'pass123'},
        content_type='application/json',
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED


@pytest.mark.django_db
def test_obtain_tokens_missing_fields(client: Client) -> None:
    response = client.post(
        _OBTAIN_URL,
        data={},
        content_type='application/json',
    )
    assert response.status_code in (
        HTTPStatus.BAD_REQUEST,
        HTTPStatus.UNAUTHORIZED,
        HTTPStatus.UNPROCESSABLE_ENTITY,
    )


@pytest.mark.django_db
def test_verify_valid_access_token(client: Client, create_user) -> None:
    token = make_jwt_token(create_user.pk)
    response = client.post(
        _VERIFY_URL,
        data={'access_token': token},
        content_type='application/json',
    )
    assert response.status_code == HTTPStatus.NO_CONTENT


@pytest.mark.django_db
def test_verify_refresh_token_rejected(client: Client, create_user) -> None:
    token = make_jwt_token(create_user.pk, token_type='refresh')
    response = client.post(
        _VERIFY_URL,
        data={'access_token': token},
        content_type='application/json',
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED


@pytest.mark.django_db
def test_verify_expired_token(client: Client, create_user) -> None:
    token = make_expired_jwt_token(create_user.pk, token_type='access')
    response = client.post(
        _VERIFY_URL,
        data={'access_token': token},
        content_type='application/json',
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED


@pytest.mark.django_db
def test_verify_incorrect_token(client: Client) -> None:
    response = client.post(
        _VERIFY_URL,
        data={'access_token': 'not.a.valid.jwt'},
        content_type='application/json',
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED


@pytest.mark.django_db
def test_refresh_valid_token(client: Client, create_user) -> None:
    refresh_token = make_jwt_token(create_user.pk, token_type='refresh')
    response = client.post(
        _REFRESH_URL,
        data={'refresh_token': refresh_token},
        content_type='application/json',
    )
    assert response.status_code == HTTPStatus.OK
    body = response.json()
    assert 'access_token' in body


@pytest.mark.django_db
def test_refresh_with_access_token_rejected(
    client: Client,
    create_user,
) -> None:
    access_token = make_jwt_token(create_user.pk, token_type='access')
    response = client.post(
        _REFRESH_URL,
        data={'refresh_token': access_token},
        content_type='application/json',
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED


@pytest.mark.django_db
def test_refresh_expired_token(client: Client, create_user) -> None:
    refresh_token = make_expired_jwt_token(create_user.pk, token_type='refresh')
    response = client.post(
        _REFRESH_URL,
        data={'refresh_token': refresh_token},
        content_type='application/json',
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED


@pytest.mark.django_db
def test_refresh_incorrect_token(client: Client) -> None:
    response = client.post(
        _REFRESH_URL,
        data={'refresh_token': 'garbage'},
        content_type='application/json',
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED


@pytest.mark.django_db
def test_logout_success(client: Client, create_user) -> None:
    headers = _auth_headers(create_user.pk)
    response = client.post(_LOGOUT_URL, **headers)
    assert response.status_code == HTTPStatus.NO_CONTENT


@pytest.mark.django_db
def test_logout_without_auth(client: Client) -> None:
    response = client.post(_LOGOUT_URL)
    assert response.status_code == HTTPStatus.UNAUTHORIZED
