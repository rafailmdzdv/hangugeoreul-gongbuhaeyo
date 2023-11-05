"""Views for day application."""
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from server.apps.days.services.study_day import responses


class StudyDayListView(APIView):
    """List view for study day."""

    def get(self, _: Request) -> Response:
        """GET method for list study days.

        :return: DRF Response
        """
        return responses.StudyDayListGETResponse().render()
