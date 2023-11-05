"""Module with `Study Days` responses."""
from typing import final

from rest_framework.response import Response

from server.apps.days.models import StudyDay
from server.services.responses import BaseResponse
from server.services.schema import FileSchema
from server.services.serializer import ModelSerializer


@final
class StudyDayListGETResponse(BaseResponse):
    """GET list of Study Days response."""

    def render(self) -> Response:
        """Render GET list of Study Days response.

        :return: Rendered response
        """
        return Response(
            ModelSerializer(
                day,
                FileSchema(day),
            ).serialize()
            for day in StudyDay.objects.all().prefetch_related('words')
        )
