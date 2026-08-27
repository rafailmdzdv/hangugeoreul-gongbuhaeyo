# Copyright © 2026 Rafail Medzhidov <rafayt323@gmail.com>
# SPDX-License-Identifier: MIT

from typing import TypedDict, final


@final
class ObtainTokensPayload(TypedDict):
    """Payload that used for tokens obtaining using email and password."""

    email: str
    password: str
