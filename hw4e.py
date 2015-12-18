# Homework for Python Web Data Course, Coursera, Dr. Chuck
# Test for HW4e, XML data extract

import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode.xml?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false','address': address})
    print 'Retrieving ', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved ',len(data), ' characters'
    print data
    tree = ET.fromstring(data)

