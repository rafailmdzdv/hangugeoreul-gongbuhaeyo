# Copyright © 2026 Rafail Medzhidov <rafayt323@gmail.com>
# SPDX-License-Identifier: MIT

from typing import TypedDict, final


@final
class UserResponse(TypedDict):
    """User response fields when calling GET /user."""

    email: str
    first_name: str
    last_name: str
    source_language: str
    avatar_url: str


@final
class UpdateUserResponse(TypedDict):
    """Response when user updated his fields."""

    success: bool


@final
class UploadAvatarResponse(TypedDict):
    """Response when user updates his avatar."""

    avatar_url: str
