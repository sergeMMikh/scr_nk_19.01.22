import json

import requests
import bs4


def read_headers(file_name='headers.json'):
    with open(file_name, 'r') as h:
        headers = json.load(h)

    return headers


def get_categories(href: str) -> dict:
    headers = read_headers()

    response = requests.get(href, headers=headers)
    text = response.text
    soup = bs4.BeautifulSoup(text, features="html.parser")

    data = soup.find('div', class_="categories__content")

    categories = data.find_all('button', class_="categories__item")

    urls_list = dict()

    for category in categories:
        name = category.get_text()
        url = category['data-url']

        urls_list.setdefault(name, url)

    return urls_list
