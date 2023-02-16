# from pprint import pprint
# from time import sleep
# import re
import requests
import bs4

from content.read_headers import read_headers


class CategoriesContentZara:
    categories_list = {}
    full_products_list = []
    headers = {}

    def get_categories(self, href: str) -> dict or str:
        self.headers = read_headers('headers.json')

        self.categories_list.clear()

        response = requests.get(href, headers=self.headers)

        text = response.text
        soup = bs4.BeautifulSoup(text, 'html.parser')

        hr2 = soup.find('head').find_all("meta")
        for met in hr2:

            if 'URL=' in str(met):
                mt = str(met).split(';')
                for m in mt:
                    if 'URL=' in m:
                        mt2 = str(mt).split("'")
                        add_url = mt2[4]

        response = requests.get(href + add_url, headers=self.headers)

        text = response.text
        soup = bs4.BeautifulSoup(text, 'html.parser')

        data = soup.find('div', class_='layout-categories__categories')

        if data:
            categories = data.find_all('li', class_="layout-categories-category")

            for category in categories:
                cat = category.find('a', class_='layout-categories-category__link link')
                name = cat.find('span', class_='layout-categories-category__name').text
                url = cat.get('href')

                self.categories_list.setdefault(name, url)

        else:
            return 'None'

        return self.categories_list
