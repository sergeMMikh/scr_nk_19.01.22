import json

import requests
import bs4

# from pprint import pprint

base_url = "https://www.nike.com/de"
url1 = base_url + "herren"
url2 = base_url + "damen"
url3 = base_url + "kinder"


def read_headers(file_name='headers.json'):
    with open(file_name, 'r') as h:
        headers = json.load(h)

    return headers


HEADERS = read_headers()

href = "https://www.nike.com/de/w/damen-gym-running-22fovz5e1x6"

response = requests.get(href, headers=HEADERS)
text = response.text
soup = bs4.BeautifulSoup(text, features="html.parser")

data = soup.find('div', class_="categories__content")

categories = data.find_all('button', class_="categories__item")

for category in categories:
    url = category['data-url']
    print(f'url: {url}')
