from dataclasses import dataclass


@dataclass
class UiConf:
    env: str

    def __post_init__(self):
        self.base_endpoint = {
            'local': 'http://localhost:5000',
            'remote': 'http://user-app:5000'
        }[self.env]
