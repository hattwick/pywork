# Read lists of hostnames from .csv and identify target subnets for capacity reclaim
# Environment: Python3.  Use Anaconda3 for future data capabilities
# Instructions: Run from same directory as input file.

import os
import csv
import socket
# import pandas as pd


# Get input file and validate input file
file = input('Type filename and press ENTER: ')
exists = os.path.isfile(file)
print('Filename read as:', file, ' and found is ', exists)

assert isinstance(exists, object)
if exists:
	with open(file) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			record = row
			print(record['Name'])
			print("Row complete")
else:
	print('File not found')