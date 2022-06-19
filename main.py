import requests
import bs4
from bs4 import BeautifulSoup

url = "https://2ip.ru/"

responce = requests.get(url)
text = responce.text

soup = bs4.BeautifulSoup(text, features="html.parser")
# print(soup)
ip_addr = soup.find(id="d_clip_button").find('span').text
print(ip_addr)

# if __name__ == '__main__':
#     pass
