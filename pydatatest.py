# Test of router list and element manipulation
# Using Python3

vendors = ['Juniper', 'Cisco', 'Arista', 'Citrix', 'NGINX', 'Timetra']

switches = ['N5K', 'N9K', 'N7K','N3K', '4507','6500','7050X']

print('\nVENDORS - no list manipulation\n')
print(vendors)

print('\nVENDORS - all members\n')
print(vendors[0:])

print('\nVENDORS - print just the last member (syntax disappears)\n')
print(vendors[-1])