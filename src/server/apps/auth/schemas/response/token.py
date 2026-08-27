# Copyright © 2026 Rafail Medzhidov <rafayt323@gmail.com>
# SPDX-License-Identifier: MIT

from typing import TypedDict, final


@final
class RefreshTokenResponse(TypedDict):
    """Response for access token refreshing."""

    access_token: str
