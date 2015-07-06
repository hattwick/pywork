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
log('Hello')
log("Network inventory", *devices)

# Keyword arguments

def remainder(number, divisor):
    return number % divisor
assert remainder(20,divisor=7) == 6
print(remainder)


#Adding timestamp to log file
def log2(message, when=datetime.now()):
    print('%s: %s' % (when,message))

log2('Test Message')

devices = ['router','switch','load_balancer','firewall']

for device in devices:
    print(device)

print ('done')