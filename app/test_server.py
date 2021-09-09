import pytest

from .server import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_basic(client):
    response = client.get('/repo/oso', headers={'user': 'graham'})
    assert response.status_code == 200
