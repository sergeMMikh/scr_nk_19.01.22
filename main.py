from pprint import pprint

from app import app, content_nike

if __name__ == '__main__':
    base_url = "https://www.nike.com/de/w/damen-gym-running-22fovz5e1x6"
    print('Categories list:')
    pprint(content_nike.get_categories(base_url))
    app.run(host="0.0.0.0")
