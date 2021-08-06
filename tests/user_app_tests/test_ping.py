import requests


def test_ping():
    r = requests.get('http://52.34.123.196:5000/login')
    assert r.status_code == 200, r.text
