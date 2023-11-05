from typing import Any, Protocol, final

import attrs
from django.db.models import Model
from jsonpath_ng import parse as json_parse

from server.services.schema import BaseSchema, FileSchema


class BaseSerializer(Protocol):
    """Base serializer."""

    def serialize(self) -> dict[str, Any]:
        """Serialize an object."""


@attrs.frozen
@final
class ModelSerializer(BaseSerializer):
    """Model serializer for Django models."""

    model: Model
    schema: BaseSchema

    def serialize(self) -> dict[str, Any]:
        """Serialize a django model."""
        fields_name_gen = (
            field_name
            for field in json_parse('$.properties').find(self.schema.load())
            for field_name in field.value.keys()
        )
        serialized_model = {}
        for field_name in fields_name_gen:
            model_field = getattr(self.model, field_name)
            # Check if field is related model
            try:
                serialized_model.update({
                    field_name: (
                        ModelSerializer(
                            related_model,
                            FileSchema(related_model),
                        ).serialize()
                        for related_model in model_field.all()
                    ),
                })
            except AttributeError:
                serialized_model.update({field_name: model_field})
        return serialized_model
