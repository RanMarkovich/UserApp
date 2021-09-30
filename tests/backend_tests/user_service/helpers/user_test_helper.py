from dataclasses import dataclass

import requests

from tests.backend_tests.user_service.config import UserConf


@dataclass
class UserTestHelper:
    config: UserConf

    def __post_init__(self):
        self.base_endpoint = self.config.base_endpoint

    def ping(self):
        r = requests.get(self.base_endpoint + '/ping')
        return r
