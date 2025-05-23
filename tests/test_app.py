from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_project.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # arrange (organização)

    response = client.get('/')  # act (ação - o teste em si)

    assert response.status_code == HTTPStatus.OK  # assert (garante resultado)
    assert response.json() == {'message': 'Olá Mundo!'}
