import json


def read_headers(file_name='headers.json'):
    with open(file_name, 'r') as h:
        headers = json.load(h)

    return headers
