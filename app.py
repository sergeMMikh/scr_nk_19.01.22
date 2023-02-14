from flask import Flask, jsonify, render_template

from content.content_nike import CategoriesContentNike

app = Flask(__name__)

content_nike = CategoriesContentNike()


@app.route('/')
def home():
    return render_template('home.html', title="Home")


@app.route('/get_categories')
def get_categories_view():
    url = "https://www.nike.com/de/w/damen-gym-running-22fovz5e1x6"
    product_categories = content_nike.get_categories(url)
    return jsonify(product_categories)


@app.route('/get_all_products')
def get_all_products_view():
    all_products = content_nike.get_all_products()
    return jsonify(all_products)


@app.route('/get_products_by_category/<name>/')
def get_product_by_category_view(name):
    products = content_nike.get_product_in_category(name, get_img=True)
    return jsonify(products)


@app.route('/get_products_by_name/<name>/')
def get_product_by_name_view(name):
    products = content_nike.get_product_by_name(name)
    return jsonify(products)
