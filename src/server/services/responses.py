"""Module with response for all project."""
from typing import Protocol

from rest_framework.response import Response


class BaseResponse(Protocol):
    """Base response protocol for [GET] request."""

    def render(self) -> Response:
        """Render a response."""
