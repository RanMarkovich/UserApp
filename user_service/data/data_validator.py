from jsonschema import validate


class DataValidator:

    @staticmethod
    def validate_payload(payload: dict, validation_schema: dict):
        try:
            validate(payload, validation_schema)
            return True, ''
        except Exception as e:
            return False, e
