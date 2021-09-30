import os
from dataclasses import dataclass

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from tests.frontend_tests.webdriver.config import Config as WebDriverConfig


@dataclass
class DriverFactory(WebDriverConfig):

    def init_driver(self):
        if self.env == 'local':
            driver = webdriver.Chrome(os.path.join(os.path.dirname(__file__), 'chromedriver'))
        elif self.env == 'remote':
            driver = webdriver.Remote(
                command_executor=self.grid_executor_base_url, desired_capabilities=DesiredCapabilities.CHROME
            )
        return driver
