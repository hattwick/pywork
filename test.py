# testing various functions in small form, some 2.x, some 3.x
# samples and variations copied or inspired by No Starch Press
# Automate the Boring Stuff with Python


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

myName = input()

print('\nNice to meet you, ' + myName)

print('The length of your name is:')
print(len(myName))

print('\nWhat is your age?')
myAge = input()
print('You will be ' + str(int(myAge)+1) + ' in a year.')


