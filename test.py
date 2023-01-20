from pprint import pprint

categories = {}


product_list = [{'s': 2}, {'d': 3}]
category_name = {"cat": product_list}

pprint(f'category_name: {category_name}')

categories.update(category_name)

pprint(f'categories: {categories}')
