__author__ = 'phil'

# Sample snippets from Harrison and Slatkin books
# work-in-progress 2015 ver.8

print('Enter your word')
word=input()
print('Checking for match pattern ...ate')
match=word.find('ate')
if (match<0):
    print('no match')
else:
    print ('match position ', match)

print('/n Moving onto file check/n')

devices = ['router','switch','load_balancer','firewall']

for device in devices:
    print(device)

print ('done')

# Moving into Logs using Variavble Positional Arguments

def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s' % (message,values_str))

log('My numbers are', [1, 2])
log('Hello', [])