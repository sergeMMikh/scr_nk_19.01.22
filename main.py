import requests
import bs4

from pprint import pprint

base_url = "https://www.nike.com/de"
url1 = base_url + "herren"
url2 = base_url + "damen"
url3 = base_url + "kinder"

HEADERS = {
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "Connection": "keep-alive",
    "Cookie": "_ga=GA1.2.2063098236.1579294195; _ym_uid=1579294195381853071; _ym_d=1641302173; \
    __gads=ID=e487ff71e75ec085-22fcd4d2dfd300ee:T=1628432062:R:S=ALNI_Maq4eBOKN_tOJTG_gcolgCNCrCksQ; \
    cto_bundle=T5t0Xl9mUmVMRWFXVUlXTWJKZVRmNWRhbHpTWjJKMSUyQiUyRnExaGR4Tzd6cXFhQUZiJTJGNE1TVExSdHc2NVdkWU5qeTgxODJqazN5Wm1nNnV5dVhaUnZUVjkwRCUyRjYyRVRVS0FCQWJjUHVXSEVxS2M3b2hyZlJYY3BsY0lJODF1NEZ6TGF1VmclMkJBT0dKc3dpMUd3T3dyJTJCelB5ckNwZGclM0QlM0Q;\
    hl=ru; fl=ru; visited_articles=531472; _gid=GA1.2.1874216268.1655576523; habr_web_home_feed=/all/; _ym_isad=2",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0"
}

href = "https://www.nike.com/de/w/jordan-schuhe-37eefzy7ok"

response = requests.get(href, headers=HEADERS)
text = response.text
soup = bs4.BeautifulSoup(text, features="html.parser")

data = soup.find('div', class_="product-grid__items css-hvew4t")

products = data.find_all('div', class_="product-card product-grid__card css-c2ovjx")

for product in products:
    product_cart = product.find('div', class_='product-card__body')
    product_img = product_cart.find('a', class_='product-card__img-link-overlay')
    aria_label = product_img.get('aria-label')
    print(f'aria_label: {aria_label}')
    href = product_img.get('href')
    print(f'href: {href}')
    product_cart_price_info = product_cart.find('div', class_='product-card__price')
    product_price = product_cart_price_info.get_text()
    print(f'product_price: {product_price}\n')

