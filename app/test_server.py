import pytest

from .server import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_basic(client):
    response = client.get("/repo/oso")
    assert response.status_code == 404

    response = client.get("/repo/gmail")
    assert response.status_code == 200


# This test will pass when we add a rule allowing public repo access
@pytest.mark.xfail
def test_public_repo(client):
    response = client.get("/repo/react")
    assert response.status_code == 200
