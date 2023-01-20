import requests
import bs4
from time import sleep

from pprint import pprint

from categories__content import read_headers, get_categories

HEADERS = read_headers()

base_url = "https://www.nike.com/de/w/damen-gym-running-22fovz5e1x6"

product_categories = get_categories(base_url)

print('product_categories')
pprint(product_categories)

for category_name, href in product_categories.items():

    print(f'category_name: {category_name}')

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
        print(f'aria_label: {aria_label}')
        href = product_img.get('href')
        print(f'href: {href}')
        product_cart_price_info = product_cart.find('div',
                                                    class_='product-card__price')

        try:
            product_price = product_cart_price_info.get_text().split("€")
            price = ''.join([i.replace(u'\xa0', u"€ ") for i in product_price])
            print(f'price: {price}\n')
        except AttributeError:
            print('NoneType')
