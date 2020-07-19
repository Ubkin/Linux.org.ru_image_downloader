#!/bin/python

import re
import requests
from bs4 import BeautifulSoup

url = 'https://www.linux.org.ru/gallery/archive'
domen = 'https://www.linux.org.ru'

def get_html(url):
    response = requests.get(url)
    return response.text 

def get_all_links(html):
    soup = BeautifulSoup(html, 'lxml')
    refs = soup.find_all('a', href=True)
    links = []
    for link in refs:
        p = link.get('href')
        links.append(p)
    return links

def sort(links):
    dates = []
    for i in links:
        if re.search(r'/gallery/archive/\d+/\d+', i):
            dates.append(i)
    return dates

def full_name(dates):
    names = []
    for i in dates:
        p = domen + i
        names.append(p)
    return names

def images(some):
    l = []
    for i in some:
        if re.search(r'https://www.linux.org.ru/images/\d+/original/\d+', i):
            l.append(i)
    return l

links = full_name(sort(get_all_links(get_html(url))))

all_links = []

for i in links:
    p = get_all_links(get_html(i))
    all_links.append(p)

images = []

for i in all_links:
    for words in i:
        z = images(words)
        images += z

for i in images:
    print(i)')')
