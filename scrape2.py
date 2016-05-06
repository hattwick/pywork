# scraping example modified from "Web Scraping with Python"
# written for Python3

import urllib
import request
from bs4 import BeautifulSoup


def gettitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html.read())
		title1 = bsObj.body.h1
	except AttributeError as e:
		return None
	return title1

title = gettitle("http://www.pythonscraping.com/pages/page1.html")
if title is None:
	print("Title not found")
else:
	print(title)
