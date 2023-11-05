"""Module with `Study Days` responses."""
from typing import final

from rest_framework.response import Response

from server.apps.days.models import StudyDay
from server.services.responses import BaseResponse


@final
class StudyDayListGETResponse(BaseResponse):
    """GET list of Study Days response."""

    def render(self) -> Response:
        """Render GET list of Study Days response.

        :return: Rendered response
        """
        return Response(
            {
                'id': day.pk,
                'title': day.title,
                'words': (
                    {
                        'id': word.pk,
                        'meaning': word.meaning,
                        'translation': word.translation,
                    }
                    for word in day.words.all()  # type: ignore
                ),
            }
            for day in StudyDay.objects.all().prefetch_related('words')
        )
