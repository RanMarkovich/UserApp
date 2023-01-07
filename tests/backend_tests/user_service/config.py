from dataclasses import dataclass


@dataclass
class UserConf:
    env: str

    def __post_init__(self):
        self.base_endpoint = {
            'local': 'http://localhost:5000',
            'remote': 'http://localhost:5000'
        }[self.env]
