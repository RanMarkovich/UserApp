import json


def load_json_file(path):
    with open(path, 'r') as f:
        response_payload = json.loads(f.read())
    return response_payload
