from http import HTTPStatus

from django.test import Client
from django.urls import reverse


def test_swagger_json(client: Client) -> None:
    """This test checks that swagger.json is accessible."""
    response = client.get(reverse('schema-json', kwargs={'format': '.json'}))
    content_type = response.headers.get('Content-Type', '')
    content_type_index = 0
    assert response.status_code == HTTPStatus.OK
    assert content_type.split(';')[content_type_index] == 'application/json'


def test_swagger(client: Client) -> None:
    """This test checks that swagger/ is accessible."""
    response = client.get(reverse('schema-swagger-ui'))
    assert response.status_code == HTTPStatus.OK
