# testing various functions in small form, some 2.x, some 3.x
# samples and variations copied or inspired by No Starch Press
# Automate the Boring Stuff with Python

import sys
import math
import time
import pprint

print('Displaying Env and Path Information\n')
# One of the most useful things this has done is flush out the python version
# Adding a statement to capture and log just that.
pprint.pprint(sys.path)


print('Enter a value to rank high or low?')
x = input()
#  x=15

if (int(x)>20):
    print("high range")
elif (int(x)>10):
    print("moderate range")
else:
    print("low range")


# Now we will get some personal information

print('\nWhat is your name?')
# myName = ('')       // Test
myName = input()

if myName == ('Phil'):
    print('\nPhil detected.  Running sys.exit')
    sys.exit()

print('\nNice to meet you, ' + myName)

print('The length of your name is:')
print(len(myName))

print('\nWhat is your age?')
myAge = input()
print('You will be ' + str(int(myAge)+1) + ' in a year.')

print()
print('Finished')

#Prepare for next exercise
