import json
from pprint import pprint

with open('headers.json', 'r') as h:
    headers = json.load(h)

print('headers')
pprint(headers)
