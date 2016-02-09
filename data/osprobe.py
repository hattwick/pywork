# Simple commands for capturing directory contents

from __future__ import print_function
import os

cwd = os.getcwd()

for folderName, subfolders, filenames in os.walk(cwd):
	print('Current folder is ' + folderName)
	print('Subfolders are ' + str(subfolders))
	print('The files ins ' + folderName + ' are: ' + str(filenames))
	print()

