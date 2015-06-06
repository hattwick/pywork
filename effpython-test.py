__author__ = 'phil'

# Sample snippets from Harrison and Slatkin books
# work-in-progress

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

# ['router','switch','load_balancer','firewall','WanOptimizer' ]
# for device in devices:
#     print (device)