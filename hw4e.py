# Homework for Python Web Data Course, Coursera, Dr. Chuck
# Test for HW4e, XML data extract
# Test input URL: http://python-data.dr-chuck.net/comments_42.xml

import urllib
import xml.etree.ElementTree as ET
from xml.parsers import expat

# parser = ET.XMLParser(encoding="utf-8")

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
#    address = raw_input('Enter location: ')
#    address =  'http://python-data.dr-chuck.net/comments_42.xml'
    address = 'http://python-data.dr-chuck.net/comments_207067.xml'

    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false','address': address})
    print 'Retrieving ', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved ',len(data), ' characters'
    print data
#    tree = ET.fromstring(data, parser = expat.ParserCreate('UTF-8'))
#    counts = tree.findall('.//count')



