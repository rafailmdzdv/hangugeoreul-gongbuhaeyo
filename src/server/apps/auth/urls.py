# Copyright © 2026 Rafail Medzhidov <rafayt323@gmail.com>
# SPDX-License-Identifier: MIT

from typing import Final

from dmr.routing import Router, path

from server.apps.auth.views import (
    LogoutController,
    ObtainTokensController,
    RefreshTokenController,
    UpdateUserAvatarController,
    UpdateUserController,
    UserController,
    VerifyTokenController,
)

app_name = 'auth'

auth_router: Final = Router(
    'auth/',
    (
        path('', ObtainTokensController.as_view(), name='authenticate'),
        path(
            'verify/',
            VerifyTokenController.as_view(),
            name='verify_access_token',
        ),
        path(
            'refresh/',
            RefreshTokenController.as_view(),
            name='refresh_token',
        ),
        path('logout/', LogoutController.as_view(), name='logout'),
    ),
    tags=['Auth'],
)

user_router: Final = Router(
    'user/',
    (
        path('', UserController.as_view(), name='user'),
        path('update/', UpdateUserController.as_view(), name='update_user'),
        path(
            'upload_avatar/',
            UpdateUserAvatarController.as_view(),
            name='upload_avatar',
        ),
    ),
)
