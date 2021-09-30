from pytest import fixture

from tests.backend_tests.user_service.config import UserConf
from tests.backend_tests.user_service.helpers.user_test_helper import UserTestHelper
from tests.frontend_tests.webdriver.driver_factory import DriverFactory


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="local",
        help="env: local or remote"
    )


@fixture
def env(request):
    return request.config.getoption("--env")


@fixture
def browser(env):
    driver_factory = DriverFactory(env)
    driver = driver_factory.init_driver()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@fixture
def user_conf(env):
    return UserConf(env)


@fixture
def user_test_helper(user_conf):
    return UserTestHelper(user_conf)
