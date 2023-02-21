import requests
from pprint import pprint

url = 'http://127.0.0.1:5000'
url = 'https://scrnk190122-production.up.railway.app/'

request = requests.post(f'{url}/product',
                        json={"url": 'https://www2.hm.com/pt_pt/productpage.1137275001.html',
                              'image': '820w',})

data_str = request.json()
print("request:")
pprint(data_str)
