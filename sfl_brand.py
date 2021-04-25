import re
import requests
from bs4 import BeautifulSoup

base_url = 'https://www.sephora.cn/'

html_doc = requests.get('https://www.sephora.cn/').text
soup = BeautifulSoup(html_doc, 'html.parser')
a_set = set()

for link in soup.find_all('a'):
    if link.get('href') is not None and link.get('href').isprintable():
        a_set.add(link.get('href'))


def url_join(url):
    base_url = 'https://www.sephora.cn/'
    all_url = ''
    try:
        if 'https' not in url:
            all_url = base_url + url
    except:
        pass
    return all_url


all_set = map(url_join, a_set)

all_set = filter(lambda x: len(x) > 10, all_set)
all_set = set(all_set)
print(all_set)

