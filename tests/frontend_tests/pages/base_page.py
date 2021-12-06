from page_objects import PageObject
from selenium.webdriver.remote.webelement import WebElement


class BasePage(PageObject):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click(self, el: WebElement):
        self.driver.wait_until(lambda f: el.is_displayed())
        el.click()

    def insert_text(self, text: str, el: WebElement):
        self.driver.wait_until(lambda f: el.is_displayed())
        el.send_keys(text)

    def get_element_css_value(self, css_prop_name: str, el: WebElement):
        self.driver.wait_until(lambda f: el.is_displayed)
        return el.value_of_css_property(css_prop_name)
