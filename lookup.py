# Read lists of hostnames from .csv and identify target subnets for capacity reclaim
# Environment: Python3.  Use Anaconda3 for future data capabilities
# Instructions: Run from same directory as input file.

import os
import csv
# import pandas as pd


# Get input file and validate input file
file = input('Type filename and press ENTER: ')
exists = os.path.isfile(file)
if exists:
    print(file, "located at ")
#    fulldata = pd.read_csv(file)
    csvfile = open(file, 'rb')
    fulldata = csv.reader(csvfile)

    print("Total rows found: {0}".format(len(fulldata), " Starting job"))
    print(fulldata)
    csvfile.close()
else:
    print(exists)