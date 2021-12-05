from dataclasses import dataclass

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager


@dataclass
class DriverFactory:
    env: str

    def __post_init__(self):
        self.grid_executor_base_url = 'http://hub:4444/wd/hub'

    def init_driver(self):
        if self.env == 'local':
            driver = webdriver.Chrome(ChromeDriverManager().install())
        elif self.env == 'remote':
            driver = webdriver.Remote(
                command_executor=self.grid_executor_base_url, desired_capabilities=DesiredCapabilities.CHROME
            )
        return driver
