# Read lists of hostnames from .csv and identify target subnets for capacity reclaim
# Environment: Python3.  Use Anaconda3 for future data capabilities
# Instructions: Run from same directory as input file.

import os
import csv
import socket

# import pandas as pd


# Get input file and validate input file
file = input('Type filename "in quotes" and press ENTER: ')
exists = os.path.isfile(file)
print('Filename read as:', file, ' and found is ', exists)

#  assert isinstance(exists, object)

iplist = []  # initialize empty list
if exists:
	with open(file) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			record = row
			try:
				ip = socket.gethostbyname(record['Name'])
				print(record['Name'], ip)
				iplist.append(ip)
			except:
				print('Name not found:', (record['Name']))
				continue

else:
	print('File not found')

print("Job complete")

# print("Unsorted IPs", iplist)