import pytest
from app import app


@pytest.fixture()
def client():
    app.config.update({
        "TESTING": True,
    })
    # other setup can go here
    with app.test_client():
        yield client

    # clean up / reset resources here


def test_app_working():
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b"Hello World"
