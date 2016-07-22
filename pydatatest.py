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
if 'Cisco' not in vendors:
	print('Cisco is missing.  Invalid list.')


# sort and then print along with total count

vendors.sort()
print('\nVENDORS - default sort\n')
print(vendors)
print('Total Count: ',len(vendors))

# copy list for future mutation
vendorcopy = vendors[:]

# now validate the copy
print('\nVENDORS - copy default sort\n')
print(vendorcopy)



# print a value range

print('\nPrinting values\n\n')
sum=0
for value in range(1,5):
	print(value)
	sum=sum+value

print('\nTotal ')
print(sum)

# Now move to a vendor-product dictionary

cisco_models = {
	'Nexus': 'Data Center Router',
	'Catalyst': 'Campus Router',
	'ASR': 'Edge Router',
}

print('\nPrinting Cisco Categories\n')

for key, value in cisco_models.items():
	print('\nBrand: ' + key)
	print(' Line ' + value)
