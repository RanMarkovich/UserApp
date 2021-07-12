from jsonschema import validate

from .common_functions import load_json_file


class DataValidator:
    _user_validation_schema = load_json_file('../schemas/user_validation_schema.json')

    def validate_user_payload(self, user_payload: dict):
        try:
            validate(user_payload, self._user_validation_schema)
            return True, ''
        except Exception as e:
            return False, e
