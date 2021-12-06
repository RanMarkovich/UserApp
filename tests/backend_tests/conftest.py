from pytest import fixture

from tests.backend_tests.user_service.config import UserConf
from tests.backend_tests.user_service.helpers.user_test_helper import UserTestHelper


@fixture
def user_conf(env):
    return UserConf(env)


@fixture
def user_test_helper(user_conf):
    return UserTestHelper(user_conf)
