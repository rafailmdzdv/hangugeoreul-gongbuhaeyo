"""Override any custom settings here."""

from server.settings.components.csp import (
    CSP_CONNECT_SRC,
    CSP_IMG_SRC,
    CSP_STYLE_SRC,
)

CSP_CONNECT_SRC += ("'self'",)
CSP_IMG_SRC += ('data:',)
CSP_STYLE_SRC += ("'self'",)
