#! python3
# Python3 utility to take clipboard contents and extract contact information
# exercise from Automate the Boring Stuff with Python

import re
# noinspection PyUnresolvedReferences
import pyperclip


# phone number pattern. using the verbose method to make it more readable

phonepattern = re.compile(r'''
(
(\d\d\d) | (\(\d\d\d\))) ?    # optional area code
(\s|-)                        # separator
\d\d\d                        # first 3 digits
-                             # separator
\d\d\d\d                      # last 4 digits
((ext(\.)?\s |x)              # word extension optional
(\d{2,4}))?                   # extension optional
)
''', re.VERBOSE)


# email regex

emailpattern = re.compile(r'''
[a-zA-Z0-9_.+]+     # name
@
[a-zA-Z0-9_.+]+     # domain
''', re.VERBOSE)


# import the clipboard
pyperclip.paste()

# extract contact information
phonenumbers = phonepattern.findall(text)
emailaddresses = emailpattern.findall(text)

allPhoneNumbers = []
for phonenumber in phonenumbers:
	allPhoneNumbers.append(phonenumber[0])

print(allPhoneNumbers)
print(emailaddresses)


# copy the contact information back to clipboard

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(emailaddresses)
pyperclip.copy(results)

# -30-
