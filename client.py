import requests
from pprint import pprint

url = 'http://127.0.0.1:5000'

request = requests.get(f'{url}/get_value')

data_str = request.json()
print("request:")
pprint(data_str)

request = requests.post(f'{url}/increment_value',
                        json={"value": 41})

data_str = request.json()
print("request:")
pprint(data_str)

request = requests.post(f'{url}/product',
                        json={"url": 'https://www.nike.com/de/t/zoom-superrep-4-next-nature-damenschuhe-fur-hiit-kurse-3wC06h/DO9837-601',
                              'title_id': 'pdp_product_title',
                              'price_div': 'product-price'})

data_str = request.json()
print("request:")
pprint(data_str)
