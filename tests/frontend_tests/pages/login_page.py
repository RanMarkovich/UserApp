from page_objects import PageElement
from selenium.webdriver.remote.webelement import WebElement

from tests.frontend_tests.pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_FIELD: WebElement = PageElement(id_='email')
    PASSWORD_FIELD: WebElement = PageElement(id_='password')
    ERROR_MESSAGE: WebElement = PageElement(xpath='//h1[contains(text(), "Login Failed!")]')
    SUCCESS_MESSAGE: WebElement = PageElement(xpath='//h1[contains(text(), "Login Success")]')

    def login(self, email: str, password: str):
        self.insert_text(email, self.EMAIL_FIELD)
        self.insert_text(password, self.PASSWORD_FIELD)
        self.EMAIL_FIELD.submit()

    def is_logged_in(self):
        return bool(self.SUCCESS_MESSAGE)
