import json
from pprint import pprint
from time import sleep

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


def get_product_in_category(category_name: str) -> dict:

    with open("products_list.json", 'r') as f:
        categories_list = f.read()

    # current_category = categories_list['Bodysuits']
    #
    # print(f'current_category: {current_category}')

    return categories_list


def get_all_products(product_categories: list) -> dict:
    products_list = []
    headers = read_headers()

    with open("products_list.json", 'w') as f:
        json.dump({}, f, ensure_ascii=False)

    for category_name, href in product_categories.items():

        product_list = []

        sleep(0.5)

        response = requests.get(href, headers=headers)
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

    return products_list
