import json
from pprint import pprint
from time import sleep

import requests
import bs4


class CategoriesContent:
    categories_list = {}
    full_products_list = []
    headers = {}

    @staticmethod
    def read_headers(file_name='headers.json'):
        with open(file_name, 'r') as h:
            headers = json.load(h)

        return headers

    def get_categories(self, href: str) -> dict:
        self.headers = self.read_headers('headers.json')

        print('headers')
        pprint(self.headers)

        self.categories_list.clear()

        response = requests.get(href, headers=self.headers)
        text = response.text
        soup = bs4.BeautifulSoup(text, features="html.parser")

        data = soup.find('div', class_="categories__content")

        categories = data.find_all('button', class_="categories__item")

        for category in categories:
            name = category.get_text()
            url = category['data-url']

            self.categories_list.setdefault(name, url)

        return self.categories_list

    def get_product_in_category(self, category_name: str) -> dict:

        # with open("products_list.json", 'r') as f:
        #     categories_list = f.read()

        # current_category = categories_list['Bodysuits']
        #
        # print(f'current_category: {current_category}')

        return {}

    def get_all_products(self) -> list:

        print('headers')
        pprint(self.headers)

        print('self.categories_list')
        pprint(self.categories_list)

        with open("products_list.json", 'w') as f:
            json.dump({}, f, ensure_ascii=False)

        for category_name, href in self.categories_list.items():

            product_list = []

            sleep(0.5)

            response = requests.get(href, headers=self.headers)
            text = response.text
            soup = bs4.BeautifulSoup(text, features="html.parser")

            data = soup.find('div', class_="product-grid__items css-hvew4t")

            products = data.find_all('div',
                                     class_="product-card product-grid__card css-c2ovjx")

            for product in products:
                product_cart = product.find('div',
                                            class_='product-card__body')
                product_img = product_cart.find('a',
                                                class_='product-card__img-link-overlay')
                aria_label = product_img.get('aria-label')
                href = product_img.get('href')
                product_cart_price_info = product_cart.find('div',
                                                            class_='product-card__price')

                price = ()
                try:
                    product_price = product_cart_price_info.get_text().split("€")
                    price = ''.join([i.replace(u'\xa0', u"€ ") for i in product_price])
                except AttributeError:
                    price = '-'
                    print('NoneType. price = "-"')

                product_dict = {'name': aria_label.replace(u'\xe4', u' '),
                                'url': href.replace(u'\xe4', u' '),
                                'price': price.replace(u'\xe4', u' ')}

                product_list.append(product_dict)

            current_category = {category_name: product_list}

            self.full_products_list.append(current_category)

            with open("products_list.json", 'a', encoding='utf-8') as f:
                try:
                    json.dump(current_category, f, ensure_ascii=False, indent=3)
                except Exception as inst:
                    print('Error record to json:')
                    pprint(current_category)
                    print(type(inst))  # the exception instance
                    print(inst.args)  # arguments stored in .args
                    print(inst)

        return self.full_products_list
