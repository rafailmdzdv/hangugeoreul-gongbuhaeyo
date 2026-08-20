from typing import TypedDict, final


@final
class ObtainTokensPayload(TypedDict):
    """Payload that used for tokens obtaining using email and password."""

    email: str
    password: str
