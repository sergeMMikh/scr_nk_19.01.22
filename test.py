# import re
# from pprint import pprint
#
# import bs4
# import requests
#
# from categories__content import CategoriesContent
#
# content = CategoriesContent()
#
# response = requests.get("https://www.nike.com/de/t/brasilia-9-5-trainingstasche-lwf29t/DM3977-010",
#                         headers=content.read_headers())
# text = response.text
# soup = bs4.BeautifulSoup(text, features="html.parser")
#
# # image = data.find_all('img', {'src': re.compile('.png')})
# images = soup.find_all('img', {'src': re.compile('.png')})
# for item in images:
#     image = item.get('src')
#     print('image: ')
#     pprint(image)
#
#     # product_list.append(product_dict)
