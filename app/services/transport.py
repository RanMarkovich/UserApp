import requests

from .config import Config


class Transport(Config):

    def register(self, payload: dict):
        r = requests.post(self._user_service_endpoint + '/register', json=payload)
        return r

    def login(self, payload: dict):
        r = requests.post(self._user_service_endpoint + '/login', json=payload)
        return r
