from datetime import datetime

import allure


class Allure:
    def __init__(self, driver):
        self.driver = driver

    def attach_screenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(),
                      name=f'screenshot_{datetime.isoformat(datetime.utcnow().replace(microsecond=0))}Z',
                      attachment_type=allure.attachment_type.PNG)
