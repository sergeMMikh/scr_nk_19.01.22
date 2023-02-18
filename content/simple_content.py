import re
import requests
import bs4

from content.read_headers import read_headers


class SimpleContentAll:
    categories_list = {}
    full_products_list = []
    headers = {}

    def get_product_data(self, data: dict) -> dict:
        self.headers = read_headers('headers.json')

        response = requests.get(data.get('url'), headers=self.headers)
        text = response.text
        soup = bs4.BeautifulSoup(text, features="html.parser")

        title = soup.find('h1', id=data.get('title_id')).text
        product_cart_price_info = soup.find('div', class_=data.get('price_div')).text

        try:
            product_price = product_cart_price_info.split("€")
            price = ''.join([i.replace(u'\xa0', u"€ ") for i in product_price])
        except AttributeError:
            price = '-'

        images_list = []
        images = soup.find_all('img', {'src': re.compile('.png')})

        for item in images:
            images_list.append(item.get('src'))

        return {"title": title,
                "price": price,
                "img": images_list}
