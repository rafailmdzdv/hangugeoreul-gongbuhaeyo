"""Serializers that used for swagger schema."""
from rest_framework.serializers import ModelSerializer

from server.apps.days.models import StudyDay, Word


class WordSerializer(ModelSerializer):
    """Word serializer used for Swagger."""

    class Meta:

        model = Word
        fields = ('id', 'meaning', 'translation')


class StudyDaySerializer(ModelSerializer):
    """Study Day serializer used for Swagger."""

    words = WordSerializer(many=True)

    class Meta:

        model = StudyDay
        fields = '__all__'
