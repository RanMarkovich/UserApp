from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_user_app_title(browser, ui_conf):
    browser.get(ui_conf.base_endpoint + '/login')
    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, "title"))
    )
    act_title = browser.title
    assert act_title == 'Login Form'
