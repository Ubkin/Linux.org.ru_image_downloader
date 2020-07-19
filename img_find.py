import re, requests
from bs4 import BeautifulSoup4 as bs

url = 'https://www.linux.org.ru/gallery/archive'
domen = 'https://www.linux.org.ru'
expression = r'/gallery/archive/\d+/\d+'
