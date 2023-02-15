from flask import Flask, jsonify, render_template

from content.content_nike import CategoriesContentNike
from content.content_zara import CategoriesContentZara

app = Flask(__name__)

content_nike = CategoriesContentNike()
content_zara = CategoriesContentZara()


@app.route('/')
def home():
    return render_template('home.html', title="Home")


@app.route('/nike/get_categories')
def nike_get_categories_view():
    url_nike = "https://www.nike.com/de/w/damen-gym-running-22fovz5e1x6"
    product_categories = content_nike.get_categories(url_nike)
    return jsonify(product_categories)


@app.route('/nike/get_all_products')
def nike_get_all_products_view():
    all_products = content_nike.get_all_products()
    return jsonify(all_products)


@app.route('/nike/get_products_by_category/<name>/')
def nike_get_product_by_category_view(name):
    products = content_nike.get_product_in_category(name, get_img=True)
    return jsonify(products)


@app.route('/nike/get_products_by_name/<name>/')
def nike_get_product_by_name_view(name):
    products = content_nike.get_product_by_name(name)
    return jsonify(products)


@app.route('/zara/get_categories')
def zara_get_categories_view():
    url_zara = "https://www.zara.com/pt/"
    product_categories_z = content_zara.get_categories(url_zara)
    return jsonify(product_categories_z)
