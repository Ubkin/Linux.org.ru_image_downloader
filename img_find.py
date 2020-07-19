import re, requests
from bs4 import BeautifulSoup

url = 'https://www.linux.org.ru/gallery/archive'
domen = 'https://www.linux.org.ru'

regex = r'/gallery/archive/\d+/\d+'
regex_img = r'https://www.linux.org.ru/images/\d+/original/\d+'

#all mouth in gallery
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

sort = search(names, regex)

total = []

for i in sort:
    total.append(get_refs(i))

img = search(total, regex_img)

for i in img:
    print(i)


#refs = BeautifulSoup(response, 'lxml').find_all('a', href=True)

#get all mouths
#for date in [ref for ref in [x.get('href') for x in refs] if re.search(regex, str(ref))]:
#    tmp = domen + str(date)
#    names.append(tmp)
#
#for i in names:
#    response = requests.get(i).text
#    refs = BeautifulSoup(response, 'lxml').find_all('a', href=True)
#    for image in [ref for ref in [x.get('href') for x in refs] if re.search(regex_img, str(ref))]:
#        print(image)
