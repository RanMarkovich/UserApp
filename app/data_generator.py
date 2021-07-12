import json

from copy import deepcopy


class DataGenerator:

    @staticmethod
    def __load_json_file(path):
        with open(path, 'r') as f:
            response_payload = json.loads(f.read())
        return response_payload

    def user(self, f_name, l_name, username, email, password):
        user_schema = deepcopy(self.__load_json_file('./schemas/user.json'))
        user_schema['firstName'] = f_name
        user_schema['lastName'] = l_name
        user_schema['userName'] = username
        user_schema['email'] = email
        user_schema['password'] = password
        return user_schema

    def login(self, email, password):
        login_schema = deepcopy(self.__load_json_file('./schemas/login.json'))
        login_schema['email'] = email
        login_schema['password'] = password
        return login_schema
