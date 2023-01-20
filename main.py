import json

import requests
import bs4
from time import sleep

from pprint import pprint

from categories__content import read_headers, get_categories

HEADERS = read_headers()

base_url = "https://www.nike.com/de/w/damen-gym-running-22fovz5e1x6"

product_categories = get_categories(base_url)

products_list = []

for category_name, href in product_categories.items():

    product_list = []

    sleep(0.5)

    response = requests.get(href, headers=HEADERS)
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

    products_list.append(current_category)

    with open("products_list.json", 'a', encoding='utf-8') as f:
        try:
            json.dump(current_category, f, ensure_ascii=False, indent=3)
        except Exception as inst:
            print('Error record to json:')
            pprint(current_category)
            print(type(inst))  # the exception instance
            print(inst.args)  # arguments stored in .args
            print(inst)

