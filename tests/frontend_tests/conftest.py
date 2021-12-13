from pytest import fixture, hookimpl

from tests.frontend_tests.config import UIConfig
from tests.frontend_tests.pages.login_page import LoginPage
from tests.frontend_tests.pages.pages import Pages
from tests.frontend_tests.pages.registration_page import RegistrationPage
from tests.frontend_tests.webdriver.driver_factory import DriverFactory
from tests.utils.allure import Allure


@hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)


@fixture  # (params=['chrome', 'firefox'])
def browser(request, env):
    driver_factory = DriverFactory(env)
    driver = driver_factory.get_driver()
    yield driver
    if request.node.rep_call.failed:
        Allure(driver).attach_screenshot()
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
