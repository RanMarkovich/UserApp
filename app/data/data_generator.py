from copy import deepcopy

from .common_functions import load_json_file


class DataGenerator:
    _user_schema = load_json_file('../schemas/user.json')
    _login_schema = load_json_file('../schemas/login.json')

    def user(self, f_name, l_name, username, email, password):
        user_schema = deepcopy(self._user_schema)
        user_schema['firstName'] = f_name
        user_schema['lastName'] = l_name
        user_schema['userName'] = username
        user_schema['email'] = email
        user_schema['password'] = password
        return user_schema

    def login(self, email, password):
        login_schema = deepcopy(self._login_schema)
        login_schema['email'] = email
        login_schema['password'] = password
        return login_schema
