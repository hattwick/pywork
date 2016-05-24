# scraping example modified from "Web Scraping with Python"
# written for Python3

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
		bsObj = BeautifulSoup(html.read(), 'html.parser')
		title = bsObj.body.h1
	except AttributeError as e:
		return None
	return title

title = getTitle("http://www.pythonscraping.com/pages/page1.html")

# First account for http and url errors
try:
	html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPError as e:
	print("HTTP error detected.")
except URLError as e:
	print("Server not found.")
else:
	print("All conditions passed")

print('//////')
bsObj = BeautifulSoup(html.read(), 'html.parser')
print(bsObj.h1)

