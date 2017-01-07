# Read lists of hostnames from .csv and identify target subnets for capacity reclaim
# Environment: Python3.  Use Anaconda3 for future data capabilities
# Instructions: Run from same directory as input file.

import os
import csv
# import pandas as pd


# Get input file and validate input file
file = input('Type filename and press ENTER: ')
# print('Filename read as:', file)
exists = os.path.isfile(file)
print(exists)
assert isinstance(exists, object)
if exists:
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
else:
    print('File not found')