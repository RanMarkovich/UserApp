import json
from os.path import join, dirname


def load_json_file(filename: str):
    abs_path = join(dirname(__file__), 'schemas/' + filename)
    with open(abs_path, 'r') as f:
        response_payload = json.loads(f.read())
    return response_payload
