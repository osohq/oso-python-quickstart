from quickstart import db, oso


def test_deny_by_default():
    assert not oso.is_allowed("alice@example.com", "GET", db[1])
