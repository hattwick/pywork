# scraping example modified from "Web Scraping with Python"
# written for Python3

from urllib.request import urlopen
import request
from bs4 import BeautifulSoup

#html = urlopen("http://www.pythonscraping.com/pages/page3.html")
html = urlopen("http://www.oscon.com/index.html")
bsObj = BeautifulSoup(html, 'html.parser')
print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())

