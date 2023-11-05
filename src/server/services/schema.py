"""Module with schemas for all project."""
import json
import re
from typing import Any, Protocol, final

import attrs
from django.db.models import Model

from server.settings.components import BASE_DIR


class BaseSchema(Protocol):
    """Base schema protocol."""

    def load(self) -> dict[str, Any]:
        """Load a schema."""


@attrs.frozen
@final
class FileSchema(BaseSchema):
    """JSON schema from file."""

    model: Model

    def load(self) -> dict[str, Any]:
        """Load a schema from json file `schema_name`.

        :return: Loaded JSON schema in Python dictionary
        """
        schema_path = BASE_DIR / 'schemas/{0}.json'.format(
            '_'.join(
                re.findall(
                    '[A-Z][^A-Z]*',
                    self.model.__class__.__name__,
                ),
            ).lower(),
        )
        return json.loads(schema_path.read_text())
