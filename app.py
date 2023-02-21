from flask import Flask, jsonify, render_template, request
from flask_json import FlaskJSON, JsonError, json_response, as_json
import functools
from content.content_nike import CategoriesContentNike
from content.content_zara import CategoriesContentZara
from content.simple_content import SimpleContentAll

app = Flask(__name__)
FlaskJSON(app)

content_nike = CategoriesContentNike()
content_zara = CategoriesContentZara()


def return_json(f):
    @functools.wraps(f)
    def inner(**kwargs):
        return jsonify(f(**kwargs))

    return inner


@app.route('/')
def home():
    return render_template('home.html', title="Home")


@app.route('/nike/get_categories')
@return_json
def nike_get_categories_view():
    url_nike = "https://www.nike.com/de/w/damen-gym-running-22fovz5e1x6"
    product_categories = content_nike.get_categories(url_nike)
    return product_categories


@app.route('/nike/get_all_products')
@return_json
def nike_get_all_products_view():
    all_products = content_nike.get_all_products()
    return all_products


@app.route('/nike/get_products_by_category/<name>/')
@return_json
def nike_get_product_by_category_view(name):
    products = content_nike.get_product_in_category(name, get_img=True)
    return products


@app.route('/nike/get_products_by_name/<name>/')
@return_json
def nike_get_product_by_name_view(name):
    products = content_nike.get_product_by_name(name)
    return products


@app.route('/zara/get_categories')
@return_json
def zara_get_categories_view():
    url_zara = "https://www.zara.com/pt/"
    product_categories_z = content_zara.get_categories(url_zara)
    return product_categories_z


@app.route('/product', methods=['POST'])
def get_simple_product_view():
    data = request.get_json(force=True)
    product_content = SimpleContentAll(data)
    return jsonify(product_content.get_product_data())


@app.route('/product/nike_test')
def get_simple_product_view_test():
    data = {"url": 'https://www.nike.com/de/t/zoom-superrep-4-next-nature-damenschuhe-fur-hiit-kurse-3wC06h/DO9837-601',
            'image': 't_PDP_1280'}
    content_ = SimpleContentAll(data)
    return jsonify(content_.get_product_data())


@app.route('/get_value')
@as_json
def get_value():
    return dict(value=12)


@app.route('/increment_value', methods=['POST'])
def increment_value():
    data = request.get_json(force=True)
    try:
        value = int(data['value'])
    except (KeyError, TypeError, ValueError):
        raise JsonError(description='Invalid value.')
    return json_response(value=value + 1)
