import re
import requests
import bs4
from content.read_headers import read_headers


def parse_price(s):
    if '.' not in s and ',' not in s:
        return float(s)

    elif s[-3] in ',.':
        dec_char = s[-3]
        sep_char = {'.': ',', ',': '.'}[dec_char]
        s = s.replace(sep_char, '')
        s = s.replace(',', '.')
        return float(s)

    else:
        s = s.replace(',', '').replace('.', '')
        return float(s)


class SimpleContentAll:
    categories_list = {}
    full_products_list = []
    headers = {}

    def __init__(self, data: dict):
        self.headers = read_headers('headers.json')
        self.data = data

        response = requests.get(self.data.get('url'), headers=self.headers)
        text = response.text
        self.soup = bs4.BeautifulSoup(text, 'lxml')

    def get_price(self):
        # Price
        print('Price')

        try:
            price = self.soup.find(class_='price').text.strip()
        except AttributeError:
            price = None

        if not price:
            try:
                price = self.soup.find(class_='Price').text.strip()
            except AttributeError:
                price = None

        # print('prices')
        spans = self.soup.find_all('span')

        for span in spans:
            if str(span).find('price') > 0:
                try:
                    print(f'span: {span}')
                    price = span.text.strip()
                    if '€' in price:
                        price = price.split('€')[0] + '€'
                        break
                except AttributeError:
                    price = None

        if not price:
            return '-'
        else:
            return price

    def get_product_data(self) -> dict:

        try:
            title = re.split("; |, ", self.soup.title.string)[0]
        except AttributeError:
            title = "-"

        print(f'title: {title}')

        # Image
        print('Image')
        images = self.soup.find_all('img')

        images_list = []
        invalid_image_list = []

        for item in images:
            if str(item).find(self.data.get('image')) > 0:
                images_list.append(item.get('src'))
            else:
                invalid_image_list.append(str(item))

        if len(images_list):
            return {"title": title,
                    "price": self.get_price(),
                    "img": images_list[0]}
        else:
            return {"title": title,
                    "price": self.get_price(),
                    "img": {"warning": f"The service didn't find images with string {self.data.get('image')}.for "
                                       f"Please check images list to find and useful tag. ",
                            "images": invalid_image_list}
                    }
