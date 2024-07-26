from http import HTTPStatus

from fastapi.testclient import TestClient

from madir.app import app


def test_root_ok_ola_mundo():
    client = TestClient(app)
    response = client.get('/ola-mundo')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olár Mundo!'}
