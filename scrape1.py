# scraping example modified from "Web Scraping with Python"
# written for Python3

import urllib.request
from bs4 import BeautifulSoup

self.soup = BeautifulSoup(html, 'html.parser')
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
