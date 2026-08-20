from typing import TypedDict, final


@final
class RefreshTokenResponse(TypedDict):
    """Response for access token refreshing."""

    access_token: str
