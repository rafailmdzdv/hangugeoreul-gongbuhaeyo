# Copyright © 2026 Rafail Medzhidov <rafayt323@gmail.com>
# SPDX-License-Identifier: MIT

from typing import TypedDict, final



@final
class UpdateUserPayload(TypedDict, total=False):
    """User fields provided to update a user."""

    first_name: str
    last_name: str
    source_language: str
