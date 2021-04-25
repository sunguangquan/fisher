import re
import requests
from bs4 import BeautifulSoup
# from lxml import html
brand_list = '<a class="NameZone"[\s\S]*?</a>'
brand_name = '<p.*?>(\w*)</p>'
# url = 'https://www.sephora.cn/brand/'
# res = requests.get(url).text
# with open('index.html', 'w') as f:
#     f.write(res)
# with open('index.html') as f:
#     res = f.read()

# brand_list = re.findall(brand_list, res)
# brand_name_list = map(lambda x: re.findall(brand_name, x), brand_list)
# brand = filter(lambda x: x != [], brand_name_list)
# brand = list(brand)
# print(brand)
# x = brand[0][0]
# product = requests.get(url + '?k=' + x).text
# soup = BeautifulSoup(product, 'html.parser')
# result = soup.find_all('a')
# brand_items = []
# for item in result:
#     if item.get('href') is not None:
#         if len(item.get('href')) > 9 and 'javascript' not in item.get('href') and 'brand' in item.get('href'):
#             brand_items.append(item)

# print(len(brand_items))


soup = BeautifulSoup(open('index.html'), 'lxml')
result = soup.find_all('a')
for item in result:
    print(item)
