from tests.backend_tests.user_service.config import UserConf
from tests.backend_tests.user_service.helpers.user_test_helper import UserTestHelper


class Services:
    def __init__(self, config):
        self.config = config

    def user_service(self):
        return UserTestHelper(self.config)


