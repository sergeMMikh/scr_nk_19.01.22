import requests
from pprint import pprint

url = 'http://127.0.0.1:5000'
# url = 'https://scrnk190122-production.up.railway.app/'

request = requests.post(f'{url}/product',
                        json={"url": 'https://de.tommy.com/archive-fit-sweatshirt-mit-bogenf%C3%B6rmigem-logo-mw0mw31069dw5',
                              'image': '31069_DW5',})

print(f"request: {request}")
data_str = request.json()
pprint(data_str)
