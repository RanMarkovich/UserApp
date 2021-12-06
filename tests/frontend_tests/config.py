from dataclasses import dataclass


@dataclass
class UIConfig:
    ENV: str

    def __post_init__(self):
        self.base_url = {
            'local': 'http://localhost:5000',
            'remote': 'http://user-app:5000'
        }[self.ENV]
        self.login_page_url = f'{self.base_url}/login'
        self.registration_page_url = f'{self.base_url}/register'
        self.user_email = 'markovich.ran@gmail.com'
        self.user_password = 'qaqa1234'
        self.first_name = 'ran'
        self.last_name = 'markovich'
        self.user_name = 'ranmarko'
