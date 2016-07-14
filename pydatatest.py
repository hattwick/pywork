# Test of router list and element manipulation
# Using Python3

vendors = ['Juniper', 'Cisco', 'Arista', 'Citrix', 'NGINX', 'Timetra']

switches = ['N5K', 'N9K', 'N7K','N3K', '4507','6500','7050X']

# Various list print methods

print('\nVENDORS - no list manipulation\n')
print(vendors)

print('\nVENDORS - all members\n')
print(vendors[0:])

print('\nVENDORS - print just the last member (syntax disappears)\n')
print(vendors[-1])

# Iterating the list removes syntax and prints each item on separate line
print('\nVENDORS - Iterate the list (once with and without .title\n')
for vendor in vendors:
	print(vendor)
	print(vendor.title())


# sort and then print along with total count

vendors.sort()
print('\nVENDORS - default sort\n')
print(vendors)
print('Total Count: ',len(vendors))

# copy list for future mutation
vendorcopy = vendors[:]


# print a value range

print('\nPrinting values\n\n')
sum=0
for value in range(1,5):
	print(value)
	sum=sum+value

print('\nTotal ')
print(sum)

