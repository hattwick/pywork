# Test of several data precision libraries.
# Includes techniques discussed in several volumes:
# "Data Wrangling with Python"

from decimal import getcontext, Decimal
import logging
logging.warning('Test Warning #####')

a = .1
b = .204

print('\nRaw float addition without decimal library')
print(a+b)

print('\nFloat addition with decimal library')

getcontext().prec = 2     # changing precision does not modify this outcome
print(a+b)


# methods for data

# method for calculating volume
def vol(rad):
    "Calculate the volume"
    return(4.0/3)*3.14*(rad**3)


def inrange(num, low, high):
    "Determine whether number is in the desired range"
    if num in range(low, high):
        print " %s is within the requested range" % str(num)
    else:
        print "The number is outside of the range."

# or just boolean check in range


def inrangeboolean(num, low, high):
    return num in range(low, high)


def parseresults(s):
    "Count the quantity of Upper and lowercase characters"
    d = {"upper": 0, "lower": 0}
    for c in s:
        if c.isupper():
            d["upper"] += 1
        elif c.islower():
            d["lower"] += 1
        else:
            pass

    print "Original string: ", s
    print "Uppercase characters: ", d["upper"]
    print "Lowercase characters: ", d["lower"]

# -30-