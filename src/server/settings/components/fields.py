"""Module that contains settings for models fields."""
import uuid

from django.utils.translation import gettext_lazy

# Params for `id` field.
DEFAULT_ID_PARAMS = {
    'verbose_name': gettext_lazy('Id'),
    'primary_key': True,
    'default': uuid.uuid4,
    'editable': False,
}
