from dmr.routing import path

from server.apps.auth.views import (
    LogoutController,
    ObtainTokensController,
    RefreshTokenController,
    VerifyTokenController,
)

app_name = 'auth'

urlpatterns = [
    path('', ObtainTokensController.as_view(), name='authenticate'),
    path(
        'verify/',
        VerifyTokenController.as_view(),
        name='verify_access_token',
    ),
    path('refresh/', RefreshTokenController.as_view(), name='refresh_token'),
    path('logout/', LogoutController.as_view(), name='logout'),
]
