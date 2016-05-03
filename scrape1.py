# scraping example modified from "Web Scraping with Python"
# written for Python3

import urllib
import request

from urllib.request import urlopen
html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())