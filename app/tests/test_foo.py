"""
Example tests for the app
"""
import json

from django.urls import reverse


def test_hello_world():
    """
    First test for the app
    :return:
    """
    assert "hello_world" == "hello_world"
    assert "foo" != "bar"


def test_ping(client):
    """

    :param client:
    :return:
    """
    url = reverse("ping")
    response = client.get(url)
    content = json.loads(response.content)
    assert response.status_code == 200
    assert content["ping"] == "pong!"
