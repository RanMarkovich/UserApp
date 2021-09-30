from dataclasses import dataclass


@dataclass
class Config:
    env: str

    def __post_init__(self):
        self.grid_executor_base_url = {
            'local': 'http://localhost:4444/wd/hub',
            'remote': 'http://hub:4444/wd/hub'
        }[self.env]
