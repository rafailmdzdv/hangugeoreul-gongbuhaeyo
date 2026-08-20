from datetime import timedelta
from enum import Enum
from http import HTTPStatus
from typing import final, override

from django.conf import settings
from django.utils import timezone
from dmr import Controller, modify
from dmr.plugins.msgspec import MsgspecSerializer
from dmr.security.jwt import request_jwt
from dmr.security.jwt.views import (
    ObtainTokensPayload as DmrObtainTokensPayload,
)
from dmr.security.jwt.views import (
    ObtainTokensResponse,
    ObtainTokensSyncController,
    RefreshTokenPayload,
    RefreshTokenSyncController,
    VerifyTokenPayload,
    VerifyTokenSyncController,
)

from server.apps.auth.auth import jwt_blocklist_auth
from server.apps.auth.dto import ObtainTokensPayload, RefreshTokenResponse


class _TokenType(Enum):
    ACCESS = 'access'
    REFRESH = 'refresh'


@final
class ObtainTokensController(
    ObtainTokensSyncController[
        MsgspecSerializer,
        ObtainTokensPayload,
        ObtainTokensResponse,
    ],
):
    """Authenticate with email and password to get JWT access and refresh tokens."""  # noqa: E501

    jwt_expiration = timedelta(seconds=settings.JWT_ACCESS_EXPIRES_IN)
    jwt_refresh_expiration = timedelta(seconds=settings.JWT_REFRESH_EXPIRES_IN)

    @override
    def convert_auth_payload(
        self,
        payload: ObtainTokensPayload,
    ) -> DmrObtainTokensPayload:
        return {
            'username': payload['email'],
            'password': payload['password'],
        }

    @override
    def make_api_response(self) -> ObtainTokensResponse:
        now = timezone.now()
        return {
            'access_token': self.create_jwt_token(
                expiration=now + self.jwt_expiration,
                token_type=_TokenType.ACCESS.value,
            ),
            'refresh_token': self.create_jwt_token(
                expiration=now + self.jwt_refresh_expiration,
                token_type=_TokenType.REFRESH.value,
            ),
        }


@final
class RefreshTokenController(
    RefreshTokenSyncController[
        MsgspecSerializer,
        RefreshTokenPayload,
        RefreshTokenResponse,
    ],
):
    """Refresh access token using refresh token."""

    jwt_expiration = timedelta(seconds=settings.JWT_ACCESS_EXPIRES_IN)

    @override
    def convert_refresh_payload(self, payload: RefreshTokenPayload) -> str:
        return payload['refresh_token']

    @override
    def make_api_response(self) -> RefreshTokenResponse:
        now = timezone.now()
        return {
            'access_token': self.create_jwt_token(
                expiration=now + self.jwt_expiration,
                token_type=_TokenType.ACCESS.value,
            ),
        }


@final
class VerifyTokenController(
    VerifyTokenSyncController[MsgspecSerializer, VerifyTokenPayload],
):
    """Validate access token."""

    @override
    def convert_verify_payload(self, payload: VerifyTokenPayload) -> str:
        return payload['access_token']


@final
class LogoutController(Controller[MsgspecSerializer]):
    """Logout and deactivate tokens."""

    auth = (jwt_blocklist_auth,)

    @modify(status_code=HTTPStatus.NO_CONTENT)
    def post(self) -> None:
        """Deactivate tokens."""
        jwt_blocklist_auth.blocklist(
            request_jwt(
                self.request,
                strict=True,
            ),
        )
