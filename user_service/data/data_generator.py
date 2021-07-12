from copy import deepcopy

from .common_functions import load_json_file


class DataGenerator:
    _user_validation_schema = load_json_file('../schemas/user_validation_schema.json')
    _login_validation_schema = load_json_file('../schemas/login_validation_schema.json')

    def user_validation_schema(self):
        user_schema = deepcopy(self._user_validation_schema)
        return user_schema

    def login_validation_schema(self):
        login_schema = deepcopy(self._login_validation_schema)
        return login_schema
