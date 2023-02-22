import requests
from pprint import pprint

# url = 'http://127.0.0.1:5000'
url = 'https://scrnk190122-production.up.railway.app/'

request = requests.post(f'{url}/product',
                        json={"url": 'https://www.amazon.es/Tommy-Hilfiger-Modern-Zapatillas-Desierto/dp/B09QB4FM7Y/ref=sr_1_1_sspa?crid=2FR01AQTOH8X0&keywords=sapatos+homem+casual&qid=1677060420&sprefix=sapatos%2Caps%2C157&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1',
                              'image': 'landingImage',})

print(f"request: {request}")
data_str = request.json()
pprint(data_str)
