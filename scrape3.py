# scraping example modified from "Web Scraping with Python"
# written for Python3

import urllib
import request
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html.read())
		title = bsObj.body.h1
	except AttributeError as e:
		return None
	return title

title = getTitle("http://www.pythonscraping.com/pages/page1.html")

if title

# First account for http and url errors
try:
	html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPError as e:
	print("HTTP error detected.")
except URLError as e:
	print("Server not found.")
else:
	print(html.read())

print('//////')
bsObj = BeautifulSoup(html.read())
print(bsObj.h1)

