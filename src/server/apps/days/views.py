"""Views for day application."""
from drf_yasg.utils import swagger_auto_schema
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from server.apps.days.serializers import StudyDaySerializer
from server.apps.days.services.study_day import responses


class StudyDayListView(APIView):
    """List view for study day."""

    @swagger_auto_schema(responses={200: StudyDaySerializer(many=True)})
    def get(self, _: Request) -> Response:
        """GET method for list study days.

        :return: Response with study days array
        """
        return responses.StudyDayListGETResponse().render()
