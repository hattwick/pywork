# Practice Exercise from McKellar Intermediate Python

from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta
import os

WORD_LIST = "sowpods.txt"
wordlist = open(WORD_LIST).readlines()
# Get rid of newlines

wordlist = [word.lower().strip() for word in wordlist]

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10}

currtime = datetime.now()
print('Current Time: ', format(currtime.strftime('%x %X')))
print('Environment: ', os.name)
print('\nWORDLIST\n')
print(wordlist)
print('\nSCORES\n')
print(scores)

# -30-
