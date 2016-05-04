# scraping example modified from "Web Scraping with Python"
# written for Python3

import urllib
import request
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

try:
	html = urlopen("http://pythonscrasddsping.com/pages/page1.html")
except HTTPError as e:
	print(e)
except URLError as e:
	print("Server not found.")
else:
	print(html.read())

print('//////')
bsObj = BeautifulSoup(html.read())
print(bsObj.h1)

