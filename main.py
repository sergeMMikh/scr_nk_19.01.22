from pprint import pprint
from flask import Flask, jsonify  # render_template

from categories__content import CategoriesContent

app = Flask(__name__)

content = CategoriesContent()


@app.route('/')
def hello():
    # return render_template('home.html')
    return ("""
    - to get a list of product categories add to IP this string: '/get_categories'<br>
    - to get all products list add this: '/get_all_products'<br>
    - to get product by name use: '/get_products_by_category/"category name"'<br>
    - to get product by name use: '/get_products_by_name/"name of product"'
    """)


@app.route('/get_categories')
def get_categories_view():
    url = "https://www.nike.com/de/w/damen-gym-running-22fovz5e1x6"
    product_categories = content.get_categories(url)
    return jsonify(product_categories)


@app.route('/get_all_products')
def get_all_products_view():
    all_products = content.get_all_products()
    return jsonify(all_products)


@app.route('/get_products_by_category/<name>/')
def get_product_by_category_view(name):
    products = content.get_product_in_category(name, get_img=True)
    return jsonify(products)


@app.route('/get_products_by_name/<name>/')
def get_product_by_name_view(name):
    products = content.get_product_by_name(name)
    return jsonify(products)


if __name__ == '__main__':
    base_url = "https://www.nike.com/de/w/damen-gym-running-22fovz5e1x6"
    print('Categories list:')
    pprint(content.get_categories(base_url))
    app.run(host="0.0.0.0")
