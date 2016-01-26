# Test of several data precision libraries.
# Includes techniques discussed in several volumes:
# "Data Wrangling with Python"

a=(.1)
b=(.204)

print('Raw float addition without decimal library\n')
print(a+b)


from decimal import getcontext, Decimal
print('\nFloat addition with decimal library\n')

getcontext().prec = 1
print(a+b)