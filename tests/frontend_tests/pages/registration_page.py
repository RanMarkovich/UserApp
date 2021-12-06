from page_objects import PageElement
from selenium.webdriver.remote.webelement import WebElement

from tests.frontend_tests.pages.base_page import BasePage


class RegistrationPage(BasePage):
    FIRST_NAME_FIELD: WebElement = PageElement(id_='fname')
    LAST_NAME_FIELD: WebElement = PageElement(id_='lname')
    USER_NAME_FIELD: WebElement = PageElement(id_='uname')
    EMAIL_FIELD: WebElement = PageElement(id_='email')
    PASSWORD_FIELD: WebElement = PageElement(id_='password')
    REGISTER_BTN: WebElement = PageElement(css='input.submitBTN')
    SUCCESS_MESSAGE: WebElement = PageElement(xpath='//h1[contains(text(), "Register Success")]')
    ERROR_MESSAGE: WebElement = PageElement(xpath='//h1[contains(text(), "Registration Failed!")]')

    def register_user(self, f_name, l_name, u_name, u_email, u_pass):
        self.driver.wait_until(lambda f: self.FIRST_NAME_FIELD.is_displayed())
        self.insert_text(f_name, self.FIRST_NAME_FIELD)
        self.insert_text(l_name, self.LAST_NAME_FIELD)
        self.insert_text(u_name, self.USER_NAME_FIELD)
        self.insert_text(u_email, self.EMAIL_FIELD)
        self.insert_text(u_pass, self.PASSWORD_FIELD)
        self.FIRST_NAME_FIELD.submit()

    def get_register_btn_background_color(self):
        return self.get_element_css_value('background-color', self.REGISTER_BTN)

    def is_registration_successful(self):
        return bool(self.SUCCESS_MESSAGE)
