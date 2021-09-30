import requests


def test_ping(user_test_helper):
    r = user_test_helper.ping()
    assert r.status_code == 200, r.text
