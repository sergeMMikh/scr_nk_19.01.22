import json
# from pprint import pprint
from time import sleep
import re
import requests
import bs4


class CategoriesContentNike:
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

    def get_product_in_category(self, category_name: str, get_img=False) -> dict:

        product_list = []

        sleep(0.5)

        response = requests.get(self.categories_list[category_name], headers=self.headers)
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

            if get_img:

                product_dict = {'name': aria_label,
                                'url': href,
                                'price': price,
                                'images': self.get_images(href)}
            else:
                product_dict = {'name': aria_label.replace(u'\xe4', u' '),
                                'url': href.replace(u'\xe4', u' '),
                                'price': price.replace(u'\xe4', u' ')}

            product_list.append(product_dict)

        current_category = {category_name: product_list}

        return current_category

    def get_all_products(self) -> list:

        self.full_products_list.clear()

        for category_name, href in self.categories_list.items():
            self.full_products_list.append(self.get_product_in_category(category_name))

        return self.full_products_list

    def get_product_by_name(self, product_name: str):

        if not self.full_products_list:
            self.get_all_products()

        products_list = []
        for category in self.full_products_list:
            for products in category.values():
                for product in products:
                    if product['name'] == product_name:
                        products_list.append(product)

        final_list = []
        for product in products_list:
            product_dict = {
                'name': product['name'],
                'url': product['url'],
                'price': product['price'],
                'images': self.get_images(product['url'])
            }
            final_list.append(product_dict)

        return final_list

    def get_images(self, url: str) -> list:

        response = requests.get(url,
                                headers=self.headers)
        text = response.text
        soup = bs4.BeautifulSoup(text, features="html.parser")

        images_list = []
        images = soup.find_all('img', {'src': re.compile('.png')})

        for item in images:
            sleep(0.5)
            images_list.append(item.get('src'))

        return images_list
