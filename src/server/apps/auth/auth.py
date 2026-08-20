from typing import Final, final

from dmr.security.jwt import JWTSyncAuth
from dmr.security.jwt.blocklist import JWTokenBlocklistSyncMixin


@final
class JWTAuthWithBlocklist(JWTokenBlocklistSyncMixin, JWTSyncAuth):
    """Authentication class that can blacklist tokens."""


jwt_blocklist_auth: Final = JWTAuthWithBlocklist()
