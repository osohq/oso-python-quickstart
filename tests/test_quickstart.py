from .conftest import test_client


def test_not_authorized(test_client):
    resp = test_client.get("/page/0")
    assert resp.status_code == 403


def test_authorized(test_client):
    resp = test_client.get("/page/2")
    assert resp.status_code == 200
