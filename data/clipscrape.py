#! python3
# Python3 utility to take clipboard contents and extract contact information

import re
import pyperclip



# TODO phone number regex
phonepattern=re.compile(r'''
(\d\d\d) | (\(\d\d\d\))) ?    # optional area code
(\s|-)                        # separator
\d\d\d                        # first 3 digits
-                             # separator
\d\d\d\d                      # last 4 digits
((ext(\.)?\s |x)              # word extension optional
(\d{2,4}))?                   # extension optional
''', re.VERBOSE)



# TODO email regex


# import the clipboard

# extract contact information

# copy the contact information back to clipboard