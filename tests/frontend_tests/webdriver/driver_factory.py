import os
from dataclasses import dataclass

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@dataclass
class DriverFactory:
    env: str

    def __post_init__(self):
        self.grid_executor_base_url = {
            'local': 'http://localhost:4444/wd/hub',
            'remote': 'http://hub:4444/wd/hub'
        }[self.env]

    def init_driver(self):
        if self.env == 'local':
            driver = webdriver.Chrome(os.path.join(os.path.dirname(__file__), 'chromedriver'))
        elif self.env == 'remote':
            driver = webdriver.Remote(
                command_executor=self.grid_executor_base_url, desired_capabilities=DesiredCapabilities.CHROME
            )
        return driver
