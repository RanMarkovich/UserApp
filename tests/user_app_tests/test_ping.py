import requests


def test_ping():
    r = requests.get('http://user-app:5000/login')
    assert r.status_code == 200, r.text
