import requests
import bs4

# from pprint import pprint

from categories__content import read_headers

base_url = "https://www.nike.com/de"
url1 = base_url + "herren"
url2 = base_url + "damen"
url3 = base_url + "kinder"

HEADERS = read_headers()

href = "https://www.nike.com/de/w/jordan-schuhe-37eefzy7ok"

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
    product_price = product_cart_price_info.get_text()
    print(f'product_price: {product_price}\n')
