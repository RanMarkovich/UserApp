from pytest import fixture
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from tests.frontend_tests.webdriver.driver_factory import DriverFactory


# @fixture
# def browser():
#     driver = webdriver.Chrome(os.path.join(os.path.dirname(__file__), 'webdriver/chromedriver'))
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()
#
#
# @fixture
# def browser_grid():
#     driver = webdriver.Remote(
#         command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME
#     )
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()


def test_user_app_title(browser):
    browser.get('http://user-app:5000/login')
    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, "title"))
    )
    act_title = browser.title
    assert act_title == 'Login Form'
