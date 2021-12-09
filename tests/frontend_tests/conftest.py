from pytest import fixture

from tests.frontend_tests.config import UIConfig
from tests.frontend_tests.pages.login_page import LoginPage
from tests.frontend_tests.pages.pages import Pages
from tests.frontend_tests.pages.registration_page import RegistrationPage
from tests.frontend_tests.webdriver.driver_factory import DriverFactory


@fixture  # (params=['chrome', 'firefox'])
def browser(env):
    driver_factory = DriverFactory(env)
    driver = driver_factory.get_driver()
    yield driver
    driver.quit()


@fixture
def login_page(browser, ui_conf):
    return LoginPage(browser)


@fixture
def registration_page(browser, ui_conf):
    return RegistrationPage(browser)


@fixture
def pages(browser):
    return Pages(browser)


@fixture
def ui_conf(env):
    return UIConfig(env)
