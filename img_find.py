import re, requests
from bs4 import BeautifulSoup

url = 'https://www.linux.org.ru/gallery/archive'
domen = 'https://www.linux.org.ru'

regex = r'/gallery/archive/\d+/\d+'
regex_img = r'https://www.linux.org.ru/images/\d+/original.jpg'

names = []

def get_refs(url):
    response = requests.get(url).text
    refs = BeautifulSoup(response, 'lxml').find_all('a', href=True)
    return [ref for ref in [x.get('href') for x in refs]]

def search(text, regex):
    return [x for x in text if re.search(regex, str(x))]

for date in get_refs(url):
    tmp = domen + str(date)
    names.append(tmp)

names = search(names, regex)

for i in names:
    for n in get_refs(i):
        if re.search(regex_img, n):
            print(n)
