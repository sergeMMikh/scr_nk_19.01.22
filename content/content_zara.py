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

    def get_categories(self, href: str) -> dict | str:
        self.headers = read_headers('headers.json')

        self.categories_list.clear()

        response = requests.get(href, headers=self.headers)
        text = response.text
        soup = bs4.BeautifulSoup(text, features="html.parser")

        data = soup.find('div', class_="notifications-header-container")

        if data:
            categories = data.find_all('button', class_="layout-categories-category__name")

            for category in categories:
                print(category)

        else:
            print('None')
        return '500 The current block is in process'
