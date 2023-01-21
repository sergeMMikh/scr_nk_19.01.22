from pprint import pprint

from flask import Flask, jsonify
from flask.views import View

from categories__content import CategoriesContent

app = Flask(__name__)

content = CategoriesContent()


class Base(View):
    def get(self, user_id: int):
        return jsonify({'Hello': 'Men!'})


@app.route('/')
def hello():
    return jsonify({'Hello': 'Men!'})


@app.route('/get_categories')
def get_categories_view():
    base_url = "https://www.nike.com/de/w/damen-gym-running-22fovz5e1x6"
    product_categories = content.get_categories(base_url)
    return jsonify(product_categories)


@app.route('/get_all_products')
def get_all_products_view():
    all_products = content.get_all_products()
    return jsonify(all_products)


# http://127.0.0.1:5000/get_products_by_category/Bodysuits
@app.route('/get_products_by_category/<name>/')
def get_product_by_category_view(name):
    # return jsonify({'Hello': name})
    products = content.get_product_in_category(name)
    return jsonify(products)


if __name__ == '__main__':
    base_url = "https://www.nike.com/de/w/damen-gym-running-22fovz5e1x6"
    print('Categories list:')
    pprint(content.get_categories(base_url))
    app.run()
