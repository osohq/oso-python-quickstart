import pytest

from app import app


@pytest.fixture(scope="module")
def test_client():
    flask_app = app
    test_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    yield test_client
    ctx.pop()
