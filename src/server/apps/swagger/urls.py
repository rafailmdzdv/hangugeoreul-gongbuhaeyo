"""Module with urls for swagger documentation."""
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        '한국어를 공부 API',
        default_version='1.0',
        contact=openapi.Contact(
            email='rafayt323@gmail.com',
            url='https://t.me/rafailka_m',
        ),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = (
    path(
        'swagger<format>/',
        schema_view.without_ui(),
        name='schema-json',
    ),
    path('swagger/', schema_view.with_ui(), name='schema-swagger-ui'),
)
