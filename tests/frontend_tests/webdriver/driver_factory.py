from dataclasses import dataclass

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, WebDriverException, \
    ElementNotInteractableException, StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@dataclass
class DriverFactory:
    ENV: str
    BROWSER: str = 'chrome'

    def __post_init__(self):
        self.grid_executor_base_url = 'http://hub:4444/wd/hub'

    def init_driver(self):
        driver = None
        if self.BROWSER == 'chrome':
            if self.ENV == 'local':
                driver = webdriver.Chrome(ChromeDriverManager().install())
            elif self.ENV == 'remote':
                driver = webdriver.Remote(
                    command_executor=self.grid_executor_base_url, desired_capabilities=DesiredCapabilities.CHROME
                )
        elif self.BROWSER == 'firefox':
            if self.ENV == 'local':
                driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            elif self.ENV == 'remote':
                pass  # TODO: add firefox grid instance
        return driver

    def get_driver(self, wait_time: int = 10):
        driver = self.init_driver()
        driver.maximize_window()
        driver.implicitly_wait(wait_time)
        driver.wait_until = lambda f, time_out=15: WebDriverWait(driver, time_out,
                                                                 ignored_exceptions=(
                                                                     NoSuchElementException, ElementNotVisibleException,
                                                                     ValueError, AttributeError, WebDriverException,
                                                                     ElementNotInteractableException,
                                                                     StaleElementReferenceException,
                                                                     ElementClickInterceptedException)).until(f,
                                                                                                              "element not found on page")
        return driver
