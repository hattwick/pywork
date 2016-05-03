# scraping example modified from "Web Scraping with Python"
# written for Python3

import urllib
import request
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())

print('//////')
bsObj = BeautifulSoup(html.read())
print(bsObj.h1)
