import re, requests
from bs4 import BeautifulSoup as bs

#List of LOR images

images = []
url = 'https://www.linux.org.ru/gallery/archive'
domen = 'https://www.linux.org.ru'
regex = r'/gallery/archive/\d+/\d+'
regex_img = r'https://www.linux.org.ru/images/\d+/original.jpg'

def get_links(url):
    response = requests.get(url).text
    refs = bs(response, 'lxml').find_all('a', href=True)
    return [x.get('href') for x in refs]

def search(url, regex):
    return [x for x in url if re.search(regex, x)]

for month in [domen + link for link in search(get_links(url), regex)]:
    for image in search(get_links(month), regex_img):
        images.append(image)

for i in set(images):
    print(i)
