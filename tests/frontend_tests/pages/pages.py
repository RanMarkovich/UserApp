from tests.frontend_tests.pages.login_page import LoginPage
from tests.frontend_tests.pages.registration_page import RegistrationPage


class Pages(LoginPage, RegistrationPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.login_page = LoginPage(driver)
        self.registration_page = RegistrationPage(driver)
