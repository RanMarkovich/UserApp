import os

from pytest import fixture
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@fixture
def browser():
    driver = webdriver.Chrome(os.path.join(os.path.dirname(__file__), 'chromedriver'))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@fixture
def browser_grid():
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME
    )
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_user_up_title(browser_grid):
    browser_grid.get('http://user-app:5000/login')
    act_title = browser_grid.title
    assert act_title == 'Login Form'
