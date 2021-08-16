import os

from pytest import fixture
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

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
        command_executor='http://hub:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME
    )
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_user_up_title(browser_grid):
    browser_grid.get('http://user-app:5000/login')
    element = WebDriverWait(browser_grid, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, "title"))
    )
    act_title = browser_grid.title
    assert act_title == 'Login Form'
