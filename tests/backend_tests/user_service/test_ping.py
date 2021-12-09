from pytest import fixture

from tests.backend_tests.init_services import Services


@fixture
def services(user_conf):
    return Services(user_conf)


def test_ping(services):
    r = services.user_service().ping()
    assert r.status_code == 200, r.text
