from flask import Flask, jsonify
from flask.views import View
from pprint import pprint

from categories__content import read_headers, get_categories, get_all_products, get_product_in_category

# product_categories = get_categories(base_url)
#
# pprint(get_all_products(product_categories))

app = Flask(__name__)


class Base(View):
    def get(self, user_id: int):
        return jsonify({'Hello': 'Men!'})


@app.route('/')
def hello():
    return jsonify({'Hello': 'Men!'})


# @app.route('/<name>')
# def hello_name(name):
#     print(f'name: {name}')
#     return jsonify({'Hello': name})


@app.route('/get_categories')
def get_categories_view():
    base_url = "https://www.nike.com/de/w/damen-gym-running-22fovz5e1x6"
    product_categories = get_categories(base_url)
    return jsonify(product_categories)


@app.route('/get_all_products')
def get_all_products_view():
    base_url = "https://www.nike.com/de/w/damen-gym-running-22fovz5e1x6"
    product_categories = get_categories(base_url)
    all_products = get_all_products(product_categories)
    return jsonify(all_products)

# http://127.0.0.1:5000/get_products_by_category/Bodysuits
@app.route('/get_products_by_category/<name>/')
def get_product_by_category_view(name):
    # return jsonify({'Hello': name})
    products = get_product_in_category(name)
    return jsonify(products)


if __name__ == '__main__':
    app.run()
